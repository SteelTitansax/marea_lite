import os
import requests
import json
import textwrap
from datetime import datetime
from utils.command_console_utils import insert_sqlite_information

# OpenWeatherMap functions
# -------------------------

def get_clima_data(ciudad, api_key,url):
    """
    Obtiene el clima actual de una ciudad usando OpenWeatherMap API
    """
    
    parametros = {
        'q': ciudad,
        'appid': api_key,
        'units': 'metric',  # Para temperatura en Celsius
        'lang': 'es'        # Para descripciones en español
    }
    
    try:
        respuesta = requests.get(url, params=parametros, timeout=10)
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return {
                'estado': 'exito',
                'datos': datos
            }
        else:
            return {
                'estado': 'error',
                'codigo_error': respuesta.status_code,
                'mensaje': respuesta.text
            }
            
    except Exception as e:
        return {
            'estado': 'error',
            'mensaje': f"Error de conexión: {str(e)}"
        }


def show_clima(datos_clima, ciudad, is_forecast=False):
    """
    Muestra la información del clima de forma legible, ya sea actual o pronóstico
    """
    if datos_clima['estado'] == 'exito':
        datos = datos_clima['datos']
        
        if is_forecast:  
            print(f"\n{'='*50}")
            print(f"🌤️ PRONÓSTICO DEL CLIMA EN {ciudad.upper()}")
            print(f"{'='*50}")
            for item in datos['list']:
                fecha = datetime.utcfromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M:%S')
                temp = item['main']['temp']
                temp_min = item['main']['temp_min']
                temp_max = item['main']['temp_max']
                descripcion = item['weather'][0]['description'].title()
                viento = item['wind']['speed']
                print(f"\n📅 {fecha}")
                print(f"🌡️  Temperatura: {temp}°C (Min: {temp_min}°C / Max: {temp_max}°C)")
                print(f"☁️  Descripción: {descripcion}")
                print(f"💨 Viento: {viento} m/s")
            print(f"{'='*50}")
        
        else:  
            sunrise = datetime.fromtimestamp(datos['sys']['sunrise']).strftime("%H:%M:%S")
            sunset = datetime.fromtimestamp(datos['sys']['sunset']).strftime("%H:%M:%S")

            print(f"\n{'='*50}")
            print(f"🌤️  CLIMA EN {ciudad.upper()}")
            print(f"{'='*50}")
            print(f"🏙️  Ciudad: {datos['name']}, {datos['sys']['country']}")
            print(f"🌡️  Temperatura: {datos['main']['temp']}°C")
            print(f"🔥 Sensación térmica: {datos['main']['feels_like']}°C")
            print(f"📉 Mínima: {datos['main']['temp_min']}°C")
            print(f"📈 Máxima: {datos['main']['temp_max']}°C")
            print(f"💧 Humedad: {datos['main']['humidity']}%")
            print(f"🌬️  Presión: {datos['main']['pressure']} hPa")
            print(f"💨 Viento: {datos['wind']['speed']} m/s")
            print(f"☁️  Descripción: {datos['weather'][0]['description'].title()}")
            print(f"👀 Visibilidad: {datos.get('visibility', 'N/A')} metros")
            print(f"☀️  Amanecer: {sunrise}")
            print(f"🌙 Atardecer: {sunset}")
            print(f"{'='*50}")
        
    else:
        print(f"\n❌ Error obteniendo datos para {ciudad}:")
        print(f"   Código: {datos_clima.get('codigo_error', 'N/A')}")
        print(f"   Mensaje: {datos_clima.get('mensaje', 'Error desconocido')}")


# CurrentAPI news  functions
# -------------------------

def currentAPI(api_key, region, language, category):
    # 🌎 Endpoint base
    url = "https://api.currentsapi.services/v1/latest-news"

    # 📋 Parámetros: idioma español
    params = {
        "region": region,
        "language": language,
        "category": category,
        "apiKey": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        news_list = data.get("news", [])

        print(f"\n📰 Últimas noticias con resumen (total: {len(news_list)})\n")

        # Just five first news
        # --------------------
        for i, article in enumerate(news_list[:5], 1):  
            title = article.get("title", "Sin título")
            description = article.get("description", "")
            summary = description.strip() or article.get("excerpt", "")

            # If no summary, we create one from the text
            # ------------------------------------------
            
            if not summary:
                summary = title[:200] + "..." if len(title) > 200 else title

            wrapped_summary = textwrap.fill(summary, width=90)

            print(f"{i}. 🗞️ {title}")
            print(f"   🧩 Resumen: {wrapped_summary}")
            print(f"   📅 Fecha: {article.get('published', 'Desconocida')}")
            print(f"   🔗 URL: {article.get('url', 'Sin enlace')}\n")
    else:
        print("❌ Error al obtener noticias:", response.status_code, response.text)


# IfixIt functions
# -------------------------
    
def get_ifixit_guides(query):
    url = f"https://www.ifixit.com/api/2.0/search/{query}"
    r = requests.get(url)
    input_data = []
    if r.status_code == 200:
        data = r.json()
        print(f"\n🔧 Resultados para '{query}':\n")
        for i, item in enumerate(data.get("results", [])[:5], 1):
            print(f"{i}. 📱 {item.get('title', 'Sin título')}")
            print(f"   🔗 {item.get('url', '')}\n")
            input_data.append({"technology": 'ifixit', "post": f"{item.get('title', 'Sin título')} : {item.get('url', '')}"})
        
        result = input("Quieres guardar los datos en la base de datos ? (Yes/No) : ")
        if "y" in result.lower() or "yes" in result.lower():
            print("entrando")
            for input_item in input_data:
                technology = input_item["technology"]
                post = input_item["post"]
                result_insert_database = insert_sqlite_information(technology,post)
                if result_insert_database:
                    print("Input insertado en la base de datos correctamente.")
    else:
        print("❌ Error al buscar guías.")

# Arxiv Science papers functions
# ---------------------------------

def get_arxiv_papers(query, max_results=5):
    input_data = []
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"    
    r = requests.get(url)
    if r.status_code == 200:
        entries = r.text.split("<entry>")
        print(f"\n📚 Papers sobre '{query}':\n")
        for entry in entries[1:]:
            title = entry.split("<title>")[1].split("</title>")[0].strip()
            link = entry.split("<id>")[1].split("</id>")[0]
            print(f"• {title}\n  🔗 {link}\n")
            input_data.append({"technology": 'arxiv', "post": f"{title} : {link}"})
        
        result = input("Quieres guardar los datos en la base de datos ? (Yes/No) : ")
        if "y" in result.lower() or "yes" in result.lower():
            for input_item in input_data:
                technology = input_item["technology"]
                post = input_item["post"]
                result_insert_database = insert_sqlite_information(technology,post)
                if result_insert_database:
                    print("Input insertado en la base de datos correctamente.")
    else:
        print("❌ Error al obtener papers de arXiv.")

# Country functions
# ---------------------------------

def get_country_info(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()[0]

        # Common_name and official
        # -------------------------------------

        common_name = data.get('name', {}).get('common', 'N/A')
        official_name = data.get('name', {}).get('official', 'N/A')

        # Capital 
        # -------------------------------------

        capital = data.get('capital', ['N/A'])
        capital = capital[0] if capital else 'N/A'

        # Population
        # -------------------------------------

        population = data.get('population', 'N/A')

        # Area
        # -------------------------------------

        area = data.get('area', 'N/A')

        # Region / Subregión
        # -------------------------------------

        region = data.get('region', 'N/A')
        subregion = data.get('subregion', 'N/A')

        # Languages (dictionary)
        # -------------------------------------

        languages = data.get('languages', {})
        languages_str = ", ".join(languages.values()) if languages else 'N/A'

        # Currency (code dictionary → data)
        # -------------------------------------

        currencies = data.get('currencies', {})
        currencies_list = []
        for code, info in currencies.items():
            name = info.get('name', '')
            symbol = info.get('symbol', '')
            currencies_list.append(f"{code} ({name} {symbol})")
        currencies_str = ", ".join(currencies_list) if currencies_list else 'N/A'

        # Timezones
        # ----------------------------

        timezones = data.get('timezones', [])
        timezones_str = ", ".join(timezones) if timezones else 'N/A'

        # Borders 
        # ----------------------------

        borders = data.get('borders', [])
        borders_str = ", ".join(borders) if borders else 'Ninguna'

        # Internet domains (tld)
        # ----------------------------

        domains = data.get('tld', [])
        domains_str = ", ".join(domains) if domains else 'N/A'

        # Flag (URL o unicode)
        # ----------------------------

        flag = data.get('flags', {}).get('svg') or data.get('flags', {}).get('png') or 'N/A'

        # ISO code — alfa-2 / alfa-3
        # ----------------------------

        cca2 = data.get('cca2', 'N/A')
        cca3 = data.get('cca3', 'N/A')

        # Display 
        # ----------------

        print("\n" + "="*60)
        print(f"🌍  País: {common_name} (Oficial: {official_name})")
        print(f"🏙️   Capital: {capital}")
        print(f"👥  Población: {population:,}")
        print(f"📐  Área: {area} km²")
        print(f"🗺️   Región: {region} / Subregión: {subregion}")
        print(f"🗣️   Idiomas: {languages_str}")
        print(f"💱  Monedas: {currencies_str}")
        print(f"🕒  Husos horarios: {timezones_str}")
        print(f"🌐  Dominios: {domains_str}")
        print(f"🔗  Fronteras: {borders_str}")
        print(f"🏷️   Códigos ISO: {cca2}, {cca3}")
        print(f"🏴  Bandera (URL o imagen): {flag}")
        print("="*60)

    else:
        print("❌ País no encontrado.")

# TMDB functions
# ----------------

def get_movie_info(api_key, query=None):
    """
    Si no se pasa 'query', muestra las películas populares.
    Si se pasa 'query', busca la información de esa película.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyApp/1.0)",
        "Accept": "application/json",
    }

    try:
        
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=es-ES&query={query}"
        r = requests.get(search_url, headers=headers, timeout=10)

        if r.status_code == 200:
            data = r.json()
            results = data.get("results", [])
            if not results:
                print("❌ No se encontró la película.")
                return

            movie = results[0]  
            movie_id = movie["id"]

            
            details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=es-ES"
            details_resp = requests.get(details_url, headers=headers, timeout=10)

            if details_resp.status_code == 200:
                details = details_resp.json()
                print("\n🎬 INFORMACIÓN DE LA PELÍCULA:")
                print(f"📖  Título: {details.get('title', 'N/A')}")
                print(f"📅  Fecha de estreno: {details.get('release_date', 'N/A')}")
                print(f"⭐  Puntuación: {details.get('vote_average', 'N/A')}")
                print(f"🕒  Duración: {details.get('runtime', 'N/A')} minutos")
                print(f"🎭  Géneros: {', '.join([g['name'] for g in details.get('genres', [])])}")
                print(f"🌎  País: {', '.join([c['name'] for c in details.get('production_countries', [])])}")
                print(f"💰  Presupuesto: ${details.get('budget', 0):,}")
                print(f"💵  Recaudación: ${details.get('revenue', 0):,}")
                print(f"📜  Descripción: {details.get('overview', 'N/A')}")
                print(f"🎞️  Página oficial: {details.get('homepage', 'N/A')}")
                print(f"🖼️  Poster: https://image.tmdb.org/t/p/w500{details.get('poster_path')}")
            else:
                print(f"❌ No se pudo obtener detalles de la película. Código {details_resp.status_code}")
        else:
            print(f"❌ Error {r.status_code}: No se pudo realizar la búsqueda de la película.")

    except requests.RequestException as e:
        print(f"❌ Error de red o solicitud: {e}")

# OpenStreetMap functions
# ------------------------

def search_place(query):
    url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json&limit=3"
    headers = {
        "User-Agent": "PDA Conversor TUI (https://tuweb-o-email-de-contacto.com)",
        "Accept": "application/json"
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            if not data:
                print("❌ No se encontraron lugares con ese nombre.")
                return
            for i, place in enumerate(data, 1):
                print(f"\n{i}. 📍 {place['display_name']}")
                print(f"   🌐 Coordenadas: ({place['lat']}, {place['lon']})")
                print(f"   🗺️  Tipo: {place.get('type', 'N/A')} | Importancia: {place.get('importance', 'N/A'):.3f}")
        elif r.status_code == 403:
            print("❌ Error 403: acceso prohibido. Nominatim requiere un encabezado 'User-Agent' válido con tu email o nombre de app.")
        else:
            print(f"❌ Error HTTP {r.status_code}: no se pudo completar la búsqueda.")
    except requests.RequestException as e:
        print(f"❌ Error de red: {e}")

# Wikipedia functions 
# -------------------------

def get_wikipedia_summary(topic):

    topic = topic.replace(" ", "_")

    url = f"https://es.wikipedia.org/api/rest_v1/page/summary/{topic}"
    headers = {
        "User-Agent": "ManuelPorteroApp/1.0 (https://github.com/manuelportero)"
    }

    try:
        input_data = []
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            print(f"\n📖 {data['title']}\n{textwrap.fill(data.get('extract', ''), width=90)}")
            print(f"🔗 {data['content_urls']['desktop']['page']}")
            input_data.append({"technology": 'wikipedia', "post": f"{data['title']}\n{textwrap.fill(data.get('extract', ''), width=90)} : {data['content_urls']['desktop']['page']}"})
        
            result = input("Quieres guardar los datos en la base de datos ? (Yes/No) : ")
            if "y" in result.lower() or "yes" in result.lower():
                for input_item in input_data:
                    technology = input_item["technology"]
                    post = input_item["post"]
                    result_insert_database = insert_sqlite_information(technology,post)
                    if result_insert_database:
                        print("Input insertado en la base de datos correctamente.")
        elif r.status_code == 404:
            print("❌ No se encontró el artículo en Wikipedia.")
        else:
            print(f"⚠️ Error {r.status_code}: No se pudo obtener el resumen.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")