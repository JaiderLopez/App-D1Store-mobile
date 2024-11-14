import flet as ft
from productos import ProductCard

# colores
rojo = "#db0616" 
rojo_oscuro = "#a10316"
blanco = "#ffffff"

class AppD1(ft.Container):
   # ---------------------------------------- CONTROLES ----------------------------------------
   def __init__(self, page):
      super().__init__()
      self.page = page
      self.page.spacing = 5
      self.page.padding = 0
      self.page.bgcolor = blanco
      self.page.fonts = {'Poppins': 'Poppins-Regular.ttf',
                         'Oswald': 'Oswald-VariableFont_wght.ttf'}
      self.page.theme = ft.Theme(scrollbar_theme= ft.ScrollbarTheme(thumb_color= rojo),
                                 font_family= 'Poppins')
      #           products list
      self.products_list = [
         ProductCard(self.page, "Pollo Marinado", "Perniles de pollo en bandeja", "assets/product01.png", 12600, 4.6, 399),
         ProductCard(self.page, "Aceite Don Olio", "Frasco aceite 2000ml", "assets/product02.png", 11400, 4.0, 399),
         ProductCard(self.page, "Brilla King", "Limpido de 2000 ml", "assets/product03.png", 4300, 4.1, 399),
         ProductCard(self.page, "Leche 200ml", "Leche Entera de 200 ml", "assets/product04.png", 2800, 4.2, 399),
         ProductCard(self.page, "Magic Friend Cachorros", "Purina para perros 1Kg", "assets/product05.png", 6900, 4.7, 399),
      ]
      self.grid_view_all = ft.GridView(runs_count=3, child_aspect_ratio=0.5,
                                       controls= self.products_list,
                                       # controls=[ft.Text("Despensa"), ft.Text("Congelados"), ft.Text("Aseo"), 
                                       #           ft.Text("Lacteos"), ft.Text("Mascotas")]
                                       )
      #           containers
      self.container_home = ft.Container(expand= True, alignment=ft.alignment.center,
                                         padding= 2,
                                         offset= ft.transform.Offset(0, 0),
                                         content= ft.Column(expand= True,
                                                   controls=[
                                                      #hanburger and profile
                                                   ft.Container(padding= 2, content= ft.Row(alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                                          controls=[
                                                             ft.Row(controls=[ft.IconButton(icon= ft.icons.MENU, icon_color= 'black'),
                                                                              ft.Image(src="assets\\D1.png", height= 30, fit= 'cover',)]),
                                                             ft.Container(ft.Image(src=r"assets\avatar.png", height=30))
                                                          ]
                                                   ), bgcolor= rojo_oscuro),
                                                      #presentation
                                                   ft.Row(height= 100, vertical_alignment= ft.CrossAxisAlignment.CENTER, alignment= ft.MainAxisAlignment.CENTER,
                                                      controls=[
                                                      ft.Text("TIENDAS\nD1", size=36, weight='bold', color= rojo, text_align= 'end',),
                                                   ft.Column(expand=True, controls=[
                                                      ft.Text("REALIZA TUS COMPRAS", size=24, weight='bold'),
                                                      ft.Text("Y RECIBE A DOMICILIO", size=18, weight='bold'),
                                                   ])]),
                                                      #search
                                                   ft.Container(alignment= ft.alignment.center, padding= 10,
                                                                content= ft.TextField(expand= True, prefix_icon=ft.icons.SEARCH, color= 'white',
                                                                                      hint_text= "Buscar producto", hint_style= ft.TextStyle(color= 'white'),
                                                                                      border_radius=10, bgcolor= rojo, border_color= 'transparent', 
                                                                                      on_change= self.filter_products, )),
                                                      #products
                                                   ft.Container(expand= True,
                                                               content= ft.Tabs( expand= True,
                                                            selected_index= 0,
                                                            indicator_color= rojo,
                                                            label_color= rojo,
                                                            tabs= [
                                                               ft.Tab(text= 'Todos',
                                                                      content= self.grid_view_all),
                                                               ft.Tab(text= 'Despensa',
                                                                      content= ft.GridView(runs_count=3, child_aspect_ratio=0.8,
                                                                      controls=[self.products_list[1]])),
                                                               ft.Tab(text= 'Congelados',
                                                                      content= ft.GridView(runs_count=3, child_aspect_ratio=0.8,
                                                                      controls=[self.products_list[0]])),
                                                               ft.Tab(text= 'Aseo',
                                                                      content= ft.GridView(runs_count=3, child_aspect_ratio=0.8,
                                                                      controls=[self.products_list[2]])),
                                                               ft.Tab(text= 'Lacteos',
                                                                      content= ft.GridView(runs_count=3, child_aspect_ratio=0.8,
                                                                      controls=[self.products_list[3]])),
                                                               ft.Tab(text= 'Mascotas',
                                                                      content= ft.GridView(runs_count=3, child_aspect_ratio=0.8,
                                                                      controls=[self.products_list[4]])),
                                                            ]
                                                                        )
                                                   )


                                                   ])
                                         )
      self.container_cart = ft.Container(expand= True, 
                                     offset= ft.transform.Offset(-2, 0),
                                     content= ft.Column(expand= True,
                                                        alignment= 'center',
                                                        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                                        controls= [
                                                           ft.Text("Products in Cart:", size= 20, font_family= 'Oswald'),
                                                           ft.Container(expand= True, alignment= ft.alignment.center,
                                                              content= ft.Image(src= "assets\\cart.gif", fit= 'cover', width= 300))
                                                        ])
                        )
      self.container_favorites = ft.Container(expand= True, 
                                     offset= ft.transform.Offset(-2, 0),
                                     content= ft.Column(expand= True,
                                                        alignment= 'center',
                                                        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                                        controls= [
                                                           ft.Text("Favorite products:", size= 20, font_family= 'Oswald'),
                                                           ft.Container(expand= True, alignment= ft.alignment.center,
                                                              content= ft.Image(src= "assets\\like.gif", fit= 'cover', width= 300))
                                                        ])
                        )
      self.container_notifications = ft.Container(expand= True, 
                                     offset= ft.transform.Offset(-2, 0),
                                     content= ft.Column(expand= True,
                                                      #   alignment= ft.MainAxisAlignment.CENTER,
                                                        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                                        controls= [
                                                           ft.Text("Notifications:", size= 20, font_family= 'Oswald'),
                                                           ft.Container(expand= True, alignment= ft.alignment.center,
                                                              content= ft.Image(src= "assets\\notification.gif", fit= 'cover', width= 300))
                                                        ])
                        )
      ... #end containers

      #           navigation botton
      ## iconos nav
      self.icon_home = ft.IconButton(icon= ft.icons.HOME, data= "1", icon_color= blanco, on_click= self.change_nav,)
      self.icon_cart = ft.IconButton(icon= ft.icons.SHOPPING_BAG, data= "2", icon_color= blanco, on_click= self.change_nav)
      self.icon_favorite = ft.IconButton(icon= ft.icons.FAVORITE, data= "3", icon_color= blanco, on_click= self.change_nav)
      self.icon_notifications = ft.IconButton(icon= ft.icons.NOTIFICATIONS, data= "4", icon_color= blanco, on_click= self.change_nav)
      ##nav
      self.nav = ft.Container(expand= True, alignment=ft.alignment.center, border_radius= 10, bgcolor= rojo_oscuro,
                              padding= 2, margin= ft.margin.only(bottom= 0),
                              content= ft.Row(alignment= ft.MainAxisAlignment.SPACE_AROUND,
                                              controls= [
                                                 self.icon_home,
                                                 self.icon_cart,
                                                 self.icon_favorite,
                                                 self.icon_notifications,
                                              ]
                                       )
                  )

      #           graphic
      self.page.add(ft.Column(expand= True, #scroll= ft.ScrollMode.AUTO,
                              controls=[
                                 ft.Stack(expand= True, #contenedor principal
                                          controls=[
                                             self.container_home,
                                             self.container_cart,
                                             self.container_favorites,
                                             self.container_notifications,
                                          ]),
                                 ft.Stack(height=50, #contenedor nav inferior
                                          controls=[
                                             self.nav
                                          ]),
                              ]

      ))
   ...

   # ---------------------------------------- FUNCIONES ----------------------------------------
   def filter_products(self, e):
      search = e.control.value.lower()
      filter_products = [
         products for products in self.products_list if search in products.title.lower()
      ]
      
      self.grid_view_all.controls = filter_products
      self.grid_view_all.update()

   def change_nav(self, e):
      data = e.control.data
      # print(datas)
      if data == "1":
         self.icon_home.bgcolor = rojo
         self.icon_cart.bgcolor = 'transparent'
         self.icon_favorite.bgcolor = 'transparent'
         self.icon_notifications.bgcolor = 'transparent'
         self.container_home.offset = ft.transform.Offset (0, 0)
         self.container_cart.offset = ft.transform.Offset (-2, 0)
         self.container_favorites.offset = ft.transform.Offset (-2, 0)
         self.container_notifications.offset = ft.transform.Offset (-2, 0)
      elif data == "2":
         self.icon_home.bgcolor = 'transparent'
         self.icon_cart.bgcolor = rojo
         self.icon_favorite.bgcolor = 'transparent'
         self.icon_notifications.bgcolor = 'transparent'
         self.container_home.offset = ft.transform.Offset (-2, 0)
         self.container_cart.offset = ft.transform.Offset (0, 0)
         self.container_favorites.offset = ft.transform.Offset (-2, 0)
         self.container_notifications.offset = ft.transform.Offset (-2, 0)
      elif data == "3":
         self.icon_home.bgcolor = 'transparent'
         self.icon_cart.bgcolor = 'transparent'
         self.icon_favorite.bgcolor = rojo
         self.icon_notifications.bgcolor = 'transparent'
         self.container_home.offset = ft.transform.Offset (-2, 0)
         self.container_cart.offset = ft.transform.Offset (-2, 0)
         self.container_favorites.offset = ft.transform.Offset (0, 0)
         self.container_notifications.offset = ft.transform.Offset (-2, 0)
      elif data == "4":
         self.icon_home.bgcolor = 'transparent'
         self.icon_cart.bgcolor = 'transparent'
         self.icon_favorite.bgcolor = 'transparent'
         self.icon_notifications.bgcolor = rojo
         self.container_home.offset = ft.transform.Offset (-2, 0)
         self.container_cart.offset = ft.transform.Offset (-2, 0)
         self.container_favorites.offset = ft.transform.Offset (-2, 0)
         self.container_notifications.offset = ft.transform.Offset (0, 0)
         
      # print(self.icon_cart.bgcolor)
      self.page.update()


def main(page: ft.Page):
   app = AppD1(page)
   # ---------------------------------------- GRAPHICS ----------------------------------------
   page.theme_mode = ft.ThemeMode.SYSTEM
   page.title = "App - D1"
   # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   page.window.min_width = 400
   page.window.min_height = 600
   page.window.width = 450
   page.window.height = 680
   page.window.max_width = 460
   page.window.max_height = 700
   
   page.add(app)

ft.app(target = main)