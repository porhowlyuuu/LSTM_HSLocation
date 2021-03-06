# coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View
# from .SQLServerConnect import *
from django.conf import settings as SET
from .ResponsDiv.util import Util
from .ResponsDiv.plsregress import Plsregress
from .ResponsDiv.optics import Optics
from .ResponsDiv.corrcoef import Corrcoef
from .ResponsDiv.excel import Excel
import os
# 功能对象
util = Util()
# 全局的电压、电流：numpy格式
IPCC, UPCC = SET.IPCC, SET.UPCC
WINDOW, STEP, PARAMS, E = SET.WINDOW, SET.STEP, SET.PARAMS, SET.E
# 当前数据是否为复数
IS_COMPLEX = SET.IS_COMPLEX
# *********测试部分*********
excel = Excel("D:\Documents\我的代码\谐波源项目\web\Location\HarmonicSourceLocation\ResponsDiv\excel\\2-2-2更新IPCC.xls",
              "D:\Documents\我的代码\谐波源项目\web\Location\HarmonicSourceLocation\ResponsDiv\excel\\2-2-2更新UPCC.xls")
data = excel.read()
IPCC, UPCC = data.get("ipcc"), data.get("upcc")
# ******************
# 最小二乘法的对象
plsregress = Plsregress(IPCC, UPCC)
# 皮尔逊相关系数的对象
corrcoef = Corrcoef(IPCC, UPCC)
# Optics聚类算法的对象
# optics是在运行 有序队列图 函数后才有值
optic = None
# 全局数据
info = SET.INFO

# 返回弹出框的html  ****废弃************


class getRespDiv(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('ResponsDiv.html')

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)


# 判断主谐波源位置
class IsClient(View):
    def get(self, request, *args, **kwargs):
        global util
        # print("&&&&:** ",eval((request.GET.getlist("test")[0])));
        yes, no = json.dumps({"res": 1}), json.dumps({"res": 0})
        try:
            ipcc = complex(dict(request.GET).get("ipcc", None)[0])
            upcc = complex(dict(request.GET).get("upcc", None)[0])
            # ipcc:一个实数或复数
            px = util.IsClinet(ipcc, upcc)
            if px:
                return HttpResponse(yes)
            else:
                return HttpResponse(no)
        except Exception as e:
            print("错误：", e)
            return HttpResponse(no)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)

# 获得简单模式的发射水平和谐波责任（均值）


class GetSimpleAver(View):
    def get(self, request, *args, **kwargs):
        global plsregress
        try:
            p_dev = plsregress.get_c_s_dev_mean()
            p_resp = plsregress.get_responsibility_mean()
            p = {**p_dev, **p_resp}
            # 分别是发射水平/责任均值
            # p= {'c_dev':i_z_mean,'s_dev':u_mean,'dc_mean':dc_mean,'ds_mean':ds_mean}
            # info.update(p)
            return HttpResponse(json.dumps({"res_p": p}))
        except Exception as e:
            print("错误：", e)
            return HttpResponse(None)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)
# 获得简单模式的发射水平和谐波责任图


class GetDrawResp(View):
    def get(self, request, *args, **kwargs):
        global plsregress
        try:
            p = plsregress.get_draw_resp()
            # 分别是发射水平/责任均值
            # p={"dc_resp":y1,"dc_len":x1,"ds_resp":y2,"ds_len":x2}
            return HttpResponse(json.dumps({"draw_p": p}))
        except Exception as e:
            print("错误：", e)
            return HttpResponse(None)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)


# 获得复杂模式的有序队列图x,y
class GetOrderData(View):
    def get(self, request, *args, **kwargs):
        global corrcoef
        global optic
        try:
            window = int(dict(request.GET).get("window", WINDOW))
            step = int(dict(request.GET).get("step", STEP))
            params = float(dict(request.GET).get("params", PARAMS))
            e = float(dict(request.GET).get("e", E))
            is_complex = IS_COMPLEX
            p = corrcoef.get_optics_data(window, step, params, is_complex)
            ipccn, upccn = p.get('ipccn'), p.get("upccn")
            # 这个时候的optics才有值
            optics = Optics(ipccn, upccn, e)
            optic = Optics(ipccn, upccn, e)
            p = optics.get_ordered_da()
            # print("********:",p)
            # 分别是可达距离、x值
            # p= {"reach_dis":y1,"times":x1}
            return HttpResponse(json.dumps({"order_p": p}))
        except Exception as e:
            print("错误GetOrderData ：", e)
            return HttpResponse(None)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)

# 获得复杂模式的三段聚类图的x,y


class GetThreeClusterData(View):
    def get(self, request, *args, **kwargs):
        global optic
        try:
            p = optic.get_three_section()
            # print("*****:", p.get("pccn_1"))
            # ipccn_1是800个值的一维list
            ''' p= {'pccn_1': [ipccn_1, upccn_1],
                'pccn_2': [ipccn_2, upccn_2],
                'pccn_3': [ipccn_3, upccn_3],
                }
            '''
            print("^^^^^^^^:", p)
            return HttpResponse(json.dumps({"three_p": p}))
        except Exception as e:
            print("错误：", e)
            return HttpResponse(None);
        # finally:
        #     return HttpResponse(json.dumps({"three_p": p}))

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)


# 获得复杂模式的三段的发射水平和责任(均值)
class GetThreeDevResp(View):
    def get(self, request, *args, **kwargs):
        global optic

        try:
            resp = optic.get_three_section_responsibility_mean()
            print("rrrr: ", resp)
            dev = optic.get_three_section_c_s_dev_mean()
            print("devvvv: ", dev)
            # 分别是责任和发射水平均值
            ''' resp={'pccn_1_resp_mean':{'dc_mean':dc_mean,'ds_mean':ds_mean} ,
                'pccn_2_resp_mean':{'dc_mean':dc_mean,'ds_mean':ds_mean}, 
                "pccn_3_resp_mean": {'dc_mean':dc_mean,'ds_mean':ds_mean}
                }
                
                dev={'dev_1':{'c_dev':i_z_mean,'s_dev':u_mean},
                'dev_2':{'c_dev':i_z_mean,'s_dev':u_mean},'dev_3':{'c_dev':i_z_mean,'s_dev':u_mean}
                }
            '''
            p = {**resp, **dev}
            print(p)

            return HttpResponse(json.dumps({"tdev_p": p}))
        except Exception as e:
            print("错误：", e)
            # return HttpResponse(None)
        finally:
            return HttpResponse(json.dumps({"tdev_p": p}))

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)
