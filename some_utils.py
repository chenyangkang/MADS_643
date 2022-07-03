def cal_alpha_length_of_str(str_):
    return len([i for i in str_ if not i=="\n" and not i==" "])

def exam_if_str_this_in(str_, test_str):
    if test_str.lower() in str_.lower():
        return True
    return False