import pandas as pd


def leer_csv(ruta_archivo):
    """
    Lee un archivo CSV y devuelve un DataFrame.
    
    Args:
        ruta_archivo (str): La ruta al archivo CSV.
        
    Returns:
        pd.DataFrame: El DataFrame que contiene los datos del CSV.
    """
    
    try:
        df = pd.read_csv(ruta_archivo, sep=',')
        return df
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return None



def retornar_balance_final(df):
    """
    Calcula el balance final a partir de un DataFrame.
    Devuelve la diferencia entre las transacciones de tipo "Crédito" y "Débito".
    
    Args:
        df (pd.DataFrame): El DataFrame que contiene los datos de las transacciones.
        
    Returns:
        float: El balance final.
    """
    
    # inicializar variables
    suma_valores_debito = None
    suma_valores_credito = None
    balance_final = None

    try:
        # calcular la suma de transacciones
        suma_valores_credito = df[df['tipo'] == 'Crédito']['monto'].sum()
        suma_valores_debito = df[df['tipo'] == 'Débito']['monto'].sum()

        # Calcular el balance final
        balance_final = suma_valores_credito - suma_valores_debito
    
    except Exception as e:
        print(f"Error al calcular el balance final: {e}")

    return balance_final



def retornar_max_transaccion(df):
    """
    Retorna la transacción con el monto máximo del DataFrame y su ID.

    Args:
        df (pd.DataFrame): El DataFrame que contiene los datos de las transacciones.
    
    Returns:
        tuple: Una tupla que contiene el ID y el monto de la transacción máxima.
    """

    # inicializar variables
    monto_maximo = None
    id_monto_maximo = None

    try:
        # Encontrar el monto máximo de la transacción
        monto_maximo = df['monto'].max()
        id_monto_maximo = df[df['monto'] == monto_maximo]['id'].values[0]
    
    except Exception as e:
        print(f"Error al encontrar la transacción máxima: {e}")

    # devolver el ID de la transacción máxima y el monto máximo
    return id_monto_maximo, monto_maximo



def retornar_conteo_transacciones(df):
    """
    Retorna el conteo de transacciones en el DataFrame.

    Args:
        df (pd.DataFrame): El DataFrame que contiene los datos de las transacciones.
    
    Returns:
        tuple: Una tupla que contiene el conteo de transacciones de crédito y débito.
    """

    # inicializar variables
    conteo_credito = None
    conteo_debito = None

    try:
        # contar el número de transacciones
        conteo_credito = len(df[df['tipo'] == 'Crédito'])
        conteo_debito = len(df[df['tipo'] == 'Débito'])
    
    except Exception as e:
        print(f"Error al contar las transacciones: {e}")

    # devolver el conteo de transacciones de crédito y débito
    return conteo_credito, conteo_debito



def reporte_transacciones(df):
    """
    Muestra un reporte de las transacciones del DataFrame.

    Args:
        df (pd.DataFrame): El DataFrame que contiene los datos de las transacciones.
    """

    if df is not None and not df.empty:
        # variables del reporte
        balance_final = retornar_balance_final(df)
        id_monto_maximo, monto_maximo = retornar_max_transaccion(df)
        conteo_credito, conteo_debito = retornar_conteo_transacciones(df)

        # Reportee
        print()
        print("Reporte de Transacciones")
        print("---------------------------------------------")
        print(f'Balance Final: {balance_final}')
        print(f'Transaccion de Mayor Monto: ID {id_monto_maximo} - {monto_maximo}')
        print(f'Conteo de Transacciones: Credito: {conteo_credito} Debito: {conteo_debito}')
        print()

    else:
        print("No hay datos para mostrar.")



if __name__ == "__main__":

    # Ruta del archivo CSV
    ruta_archivo = 'example.csv'
    df = leer_csv(ruta_archivo)
    
    # Generar el reporte de transacciones
    if df is not None:
        reporte_transacciones(df)

    else:
        print("No se pudo leer el archivo CSV.")