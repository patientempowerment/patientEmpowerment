from ml import model_objects, imputer, dataframe_column_labels

# converts
def get_model_dict(label):
    model = model_objects[label]
    feature_names = dataframe_column_labels.copy()
    label_index = feature_names.index(label)
    del(feature_names[label_index])
    feature_means = imputer.initial_imputer_.statistics_.copy().tolist()
    del(feature_means[label_index])
    weights = model.coef_
    model_dict = dict()
    model_dict["intercept"] = model.intercept_[0]
    features_dict = dict()
    for i, feature_name in enumerate(feature_names):
        feature_dict = dict()
        feature_dict["coef"] = weights[0][i]
        feature_dict["mean"] = feature_means[i]
        features_dict[feature_name] = feature_dict
    model_dict["features"] = features_dict
    return model_dict