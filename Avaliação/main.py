import pandas as pd
# Funcoes
def VerificaAno(sites: pd.DataFrame, id: list) -> pd.DataFrame:
    return sites.loc[sites['Site ID'].isin(id)]

def Ordem(qualidade: pd.DataFrame) -> pd.DataFrame:
    qualidade = qualidade.sort_values(by=['State'])
    return qualidade


def VerificacoesData(results: pd.DataFrame) -> pd.DataFrame:
    verificacao = results.loc[results['Alerts'] == 'Yes']
    for id, value in verificacao.iterrows():
        if value['Mbps'] < 10:
            print(f'O Site ID {value["Site ID"]} tem uma velocidade menor que 10 mbps')

        print(f'O Site ID {value["Site ID"]} esta em alerta')

    print('A media de qualidade dos sites é: ', results["Quality (0-10)"].median())


# Final Funcoes

excel_results = pd.read_excel('Results.xlsx')
excel_sites = pd.read_excel('SiteList.xlsx')

listaId = excel_sites['Site ID'].tolist()
sites_df = VerificaAno(excel_results, listaId)
results_df = VerificacoesData(excel_results)
sites_df = Ordem(sites_df)
sites_df.to_excel('quality-report-2023.xlsx')

