import pandas as pd

class Regressor:

    def get_predictions(self, area_type, location, size, total_sqft, bath, model):
        size = size + 2
        data = pd.DataFrame([[area_type, location, size, total_sqft, bath]], 
                            columns=['area_type', 'location', 'size', 'total_sqft', 'bath'])
        prediction = model.predict(data)
        return prediction[0]
