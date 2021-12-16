import os
import dill
import pandas as pd


class Model():
    
# Инициализация (путь к файлу модели, путь к файлу с результатами)
    def __init__(self, path_model: str, path_result: str) -> None:
        self.path_model = path_model
        self.file_out_result = path_result

        # Загрузка модели
        with open(self.path_model, 'rb') as file:
            self.model = dill.load(file)

# Запуск модели (путь к data_test)
    def run(self, path_data: str) -> None:
        
        df_init = pd.read_csv(path_data)

        df = pd.DataFrame()
        df[['id', 'vas_id', 'buy_time']] = df_init[['id', 'vas_id', 'buy_time']]
        df['target'] = self.model.predict_proba(df_init)[:,1]
        df.to_csv(self.file_out_result)


if __name__ == '__main__':

    megafon = Model(
        path_model='model.dill',
        path_result='answers_test.csv'
    )
    megafon.run(path_data='data_test.csv')
