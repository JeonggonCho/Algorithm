def solution(data, ext, val_ext, sort_by):
    contents = ["code", "date", "maximum", "remain"]
    ext_li = []
    for i in data:
        if i[contents.index(ext)] <= val_ext:
            ext_li.append(i)
    answer = sorted(ext_li, key = lambda x : x[contents.index(sort_by)])
    return answer