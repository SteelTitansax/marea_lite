from utils.api_utils import get_clima_data, show_clima, currentAPI, get_wikipedia_summary,get_movie_info,get_ifixit_guides,get_country_info,get_clima_data,get_arxiv_papers, search_place
from config import settings
from constants import num_layout_equals, clima_url, forecast_url
import os

def api_information_search():

    
    while True:
        try: 

            # ❌ Clean screen
            # ----------------

            os.system("clear")

            print("=" * num_layout_equals)
            print("🌐 CONSOLA DE APIs GRATUITAS - MULTIPROPÓSITO")
            print("=" * num_layout_equals)
            print("Consola de APIs para información en tiempo real - Autor: Manuel Portero Leiva")
            print("=" * num_layout_equals)
            print("Selecciona una API para consultar:")
            print("=" * num_layout_equals)
            print("🌤️   Opción 1: OpenWeatherMap - Clima actual de cualquier ciudad")
            print("🧠  Opción 2: CurrentsAPI - Noticias internacionales (en español)")
            print("🧰  Opción 3: iFixit - Guías de reparación de dispositivos")
            print("📚  Opción 4: arXiv - Búsqueda de papers científicos")
            print("🌍  Opción 5: RestCountries - Datos de todos los países del mundo")
            print("🎬  Opción 6: TMDB - Películas más populares")
            print("🗺️   Opción 7: OpenStreetMap - Búsqueda de lugares y direcciones")
            print("📖  Opción 8: Wikipedia - Resúmenes de artículos")
            print("👋  Opción 9: Salir")
            print("=" * num_layout_equals)
            

            answer = input("🌐  Seleccion API : ").strip()

            match(answer):
            
                # 🌤️ Clima
                # ----------------
                case "1":
                    while True: 
                        try:
                            print("🌤️ Mostrando información relativa al clima ...")
                            city = input("🏙️  Ciudad : ") 
                            if not(city == ""):
                                result = get_clima_data(city, settings.api_settings.OPENWEATHER, clima_url)
                                show_clima(result, city, is_forecast=False)
                                forecast_result = get_clima_data(city, settings.api_settings.OPENWEATHER, forecast_url)
                                show_clima(forecast_result, city, is_forecast=True)
                            else:
                                print("Introduce una ciudad valida")

                        except Exception as e:
                            print(f"Error: {e}")

                        exit_question = input ("Deseas parar de buscar información (Yes/No)")
                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break


                # 📰 Noticias (CurrentsAPI)
                # ----------------

                case "2":
                    while True:
                        try:

                            print("📰 Mostrando noticias relevantes de hoy ...")
                            language = input("Idioma (es, fr, en, de, it): ")
                            category = input("Categoría (technology, science, world, politics, sports, business, health, entertainment): ")
                            region = input("Región (ES,IT,FR,etc...)")

                            if not(language) == "" or not(region) == "" or not(category) == "":
                                currentAPI(settings.api_settings.CURRENTAPI, region, language, category)
                            else:
                                print("Por favor, Introduce lenguage y categoria correctas")
                        except Exception as e:
                            print(f"Error: {e}")

                        exit_question = input ("Deseas parar de buscar información (Yes/No)")
                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break

                # 🧰 iFixit
                # ----------------

                case "3":
                    while True :
                        try:
                            print("🔧 Mostrando documentos de reparacion en iFixit ...")
                            query = input("Dispositivo o tema a buscar (ej: iPhone, Laptop, PlayStation): ")
                            if not(query) == "" :
                                get_ifixit_guides(query)
                            else:
                                print("Por favor introduczca un parámetro de búsqueda válido")

                        except Exception as e:
                            print(f"Error: {e}")

                        exit_question = input ("Deseas parar de buscar información (Yes/No)")
                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break


                # 📚 arXiv
                # ----------------

                case "4":
                    while True:
                        try:
                            print("🔬 Mostrando noticias de invstigación ...")
                            query = input("🔢 Tema o palabra clave (ej: quantum computing, AI, physics): ") 
                            max_results = input("🔢 Cantidad de resultados (Enter para 5): ") 
                            if max_results == "" :
                                max_results = "5"
                            if not(query == ""):  
                                get_arxiv_papers(query, int(max_results))
                            else: 
                                print("Por favor, introduzca un parámetro de búsqueda válido")
                        except Exception as e:
                            print(f"Error: {e}")

                        exit_question = input ("Deseas parar de buscar información (Yes/No)")
                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break

                # 🌍 RestCountries
                # ----------------

                case "5":
                    while True:
                        try:
                            print("🌍 Mostrando informacón sobre paises...")
                            country = input("Nombre del país (ej: Spain, France, Germany): ")
                            if not(country == ""):
                                get_country_info(country)
                            else:
                                print("Por favor introduzca un país válido")

                        except Exception as e:
                            print(f"Error: {e}")

                        exit_question = input ("Deseas parar de buscar información (Yes/No)")
                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break


                # 🎬 TMDB
                # ----------------

                case "6":
                    while True:
                        try:
                            print("🎬 Mostrando películas más populares...")
                            film = input("Pelicula de búsqueda: ") 
                            if not(film == ""):
                                get_movie_info(settings.api_settings.TMDB,film)
                            else:
                                print("Por favor introduzca una película valida")

                        except Exception as e:
                                print(f"Error: {e}")

                        exit_question = input ("Deseas parar de buscar información (Yes/No)")
                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break

                # 🌍  OpenStreetMap
                # ----------------

                case "7":
                    while True:
                        try:
                            print("🌍 Mostrando ubicaciones ...")
                            query = input("Siito de busqueda: ") 
                            if not(query == ""):
                                search_place(query)
                            else:
                                print("Por fvor introduzca una ubicación valida")

                        except Exception as e:
                                print(f"Error: {e}")

                        exit_question = input ("Deseas parar de buscar información (Yes/No)")
                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break

                # 📖 Wikipedia
                # ----------------

                case "8":
                    while True:
                        try:
                            topic = input("📖 Tema a consultar en Wikipedia: ")
                            if not(topic == ""):
                                get_wikipedia_summary(topic)
                            else:
                                print("Por favor introduzca un tema válido")

                        except Exception as e:
                                print(f"Error: {e}")

                        exit_question = input ("Deseas parar de buscar información (Yes/No)")
                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break

                # 👋 Exit
                # ----------------

                case "9":
                    print("Saliendo de la consola de APIs.")
                    break
                    break # first break , breaks the match/case, second breaks the while
            
                # 🧭 Opción no válida
                # ----------------
                
                case _:
                    print("❌ Opción no válida. Intenta de nuevo.\n")

            # 👋 Exit Dialog
            # ----------------

            option_break = input("Deseas salir de la consola de APIs ? (Yes/No): ")
            
            if option_break.lower() == "y" or option_break.lower() == "yes":
                break
                break # the first break, breaks the match case , the second break the while
                

        except Exception as e:
            print(f"❌ Error de seleccion: {e}")    