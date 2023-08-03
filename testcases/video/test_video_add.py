# # @Time   ：2023/3/17 15:46
# # @Author : Chao
# # @File   : test_video_add.py
#
# import allure
# from aikn_api.video_add import video_add
# from aikn_api.video_upload import video_upload
# from aikn_api.class_search import class_search
# from aikn_api.field_search import field_search
# import requests
#
# @allure.epic("知识库")
# @allure.feature("知识")
# @allure.story("视频库")
# @allure.title("新增视频知识成功")
# def test_video_add(login_fixture, base_url, random_fixture):
#
#     # <editor-fold desc = "class, field, upload">
#     r1 = class_search(login_fixture, base_url, domain_id=str(18)).json()
#     _class_id_ = str(r1['data'][0]['id'])
#
#     r2 = field_search(login_fixture, base_url).json()
#     _field_id_ = str(r2['data'][0]['id'])
#     _open_field_id_ = str(r2['data'][0]['id'])
#
#     r3 = video_upload(login_fixture, base_url, file_path = '/Users/iyunwen/Desktop/zhishiku-stable/video/Grass.mp4').json()
#     _video_id_ = r3['data'][0]['id']
#     _cover_id_ = r3['data'][1]['id']
#     _video_time_ = r3['data'][0]['videoTime']
#     _url_ = r3['data'][0]['url']
#     print(r3)
#     # </editor-fold>
#
#     _r_ = video_add(login_fixture, base_url, video_id = _video_id_, cover_id = _cover_id_, video_time = _video_time_,
#                     video_src = _url_, class_id = _class_id_, field_id = _field_id_, open_field_id = _open_field_id_,
#                     video_name = random_fixture("视频"))
#     print(r.text)
#     assert 视频库分类()["code"] == 1
#     assert r.status_code == 200
#     assert 视频库分类()['message'] == '操作成功!'