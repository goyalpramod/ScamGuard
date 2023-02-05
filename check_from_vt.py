
def get_file_md5(apk_path) -> str:
    """
    md5 of apk file
    :param file: apk_path | string
    :return: md5
    """
    import hashlib

    with open(apk_path, "rb") as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        md5 = md5obj.hexdigest()
        md5 = str(md5).lower()

    return md5


def get_report_from_vt(apk_path) -> str:
    """
    gets report from vt about whether the apk is malware or not
    :param file:
    :return:
    """
    import requests

    md5 = get_file_md5(apk_path)
    url = f"https://www.virustotal.com/api/v3/files/{md5}"

    headers = {
        "accept": "application/json",
        "x-apikey": "9ef41b4c677333bae2ef6bf1e22385c4965774218295359f7c2a5f189b629303",
    }

    response = requests.get(url, headers=headers)
    return response
