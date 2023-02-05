def get_permission(apk_path) -> str:
    """
    takes the apk path as input and returns all the permissions required by that apk
    :param file: apk_path | string
    :return: permissions | list
    """
    from androguard.misc import AnalyzeAPK

    a, d, dx = AnalyzeAPK(apk_path)
    store = a.get_permissions()
    return store



def create_test_from_permissions(permissions) -> list[str]:
    '''
    takes in raw permissions processes them and returns a dataframe on which the data is to be tested 
    :param file: permissions | list[str]
    :return: dataframe
    '''
    import pickle
    import pandas as pd
    import numpy as np 

    result = []

    for permission in permissions:
        # print(permission)
        temp_arr = permission.split(".")
        result.append(temp_arr[-1])

    with open("column_names", "rb") as fp:   # Unpickling
        column_name = pickle.load(fp)

    d = pd.DataFrame(0, index=np.arange(1), columns=column_name)

    for permission in result: 
        if permission in column_name:
            d.at[0,"{}".format(permission)]=1
    
    return d
    
    
def fraud_from_apk_file(apk_path) -> str:
    """
    uses the ml model to predict whether the apk is malware of not from the permissions
    :param file: path of the apk file | string
    :return: fraud or not | boolean
    """
    from keras.models import load_model
    import numpy as np

    model = load_model("model.h5")
    permissions = get_permission(apk_path=apk_path)
    testX = create_test_from_permissions(permissions=permissions)
    #  check testX once
    y_pred = model.predict(testX)
    y_pred_class = np.argmax(y_pred, axis=1)
    return y_pred_class
