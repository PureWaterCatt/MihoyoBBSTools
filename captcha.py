import httpx


def game_captcha(gt: str, challenge: str):
    return None  # 失败返回None 成功返回validate


def bbs_captcha(gt: str, challenge: str):
    res = httpx.get("http://nine:9645/pass_nine",
                    params={'gt': gt, 'challenge': challenge, 'use_v3_model': True, "save_result": False}, timeout=10)
    datas = res.json()['data']
    if datas['result'] == 'success':
        return datas['validate']
    return None  # 失败返回None 成功返回validate
