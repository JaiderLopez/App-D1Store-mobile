import flet as ft

class ProductView(ft.View):
   def __init__(self, product):
      super().__init__(bgcolor= ft.colors.TRANSPARENT)
      self.product = product
      
      self.controls = [
         ft.Container(expand= True, alignment= ft.alignment.center, bgcolor= "#0b0e13",
                  margin= 10, padding= 10,
                  content= ft.Column(expand= True, horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                           alignment= ft.MainAxisAlignment.CENTER,
                           # scroll= ft.ScrollMode.AUTO,
                           controls= [
                              ft.Stack(expand= 9, 
                                 controls=[
                                    ## img product
                                    ft.Container(alignment= ft.alignment.center, border_radius= 0, #bgcolor= "red",
                                             content= ft.Image(src= self.product.img_src, width= 300, 
                                                               height= 400, fit= 'cover', border_radius= 15,)
                                    ),
                                    ## back and close view option
                                    ft.Container(content=ft.Row([ft.Icon(name= ft.icons.KEYBOARD_ARROW_LEFT,),
                                             ft.Text("Volver", color= 'white',)]), on_click= self.close_view,
                                             offset= ft.transform.Offset(0, 0),
                                    ),
                                    ## descripcion product
                                    ft.Container(expand= True, alignment= ft.alignment.center_left, bgcolor= ft.colors.with_opacity(0.4, 'black'),
                                                padding= 20, margin= ft.margin.only(top= 200), shadow= ft.BoxShadow(
                                                                                                         spread_radius= 15,
                                                                                                         blur_radius= 20,
                                                                                                         color= ft.colors.with_opacity(0.3, 'black'),
                                                                                                         # offset= ft.transform.Offset(0, 0)
                                                                                                      ), border_radius= 20,
                                                content= ft.Column(spacing= 10, controls= [
                                                                                 ft.Text(value= self.product.title, size= 30, weight= 'bold', color= 'white'),
                                                                                 ft.Text(value= self.product.description, size= 15, weight= 'w400', color= 'white'),
                                                                                 ft.Row(spacing= 5, 
                                                                                          controls=[
                                                                                             ft.Icon(name= ft.cupertino_icons.MONEY_DOLLAR, color= ft.colors.YELLOW_100),
                                                                                             ft.Text(value= str(self.product.price), weight= 'bold', color= ft.colors.YELLOW_400)
                                                                                             ]
                                                                                 ),
                                                                                 ft.Text(value= f"Stock: {self.product.stock}", size= 20, weight= 'bold', color= 'white'),
                                                                              ]
                                                         )
                                    ),
                                 ]
                              ),
                              ft.Container(height= 25, alignment= ft.alignment.center_left,
                                           content= ft.Text("Opciones:", color= 'white', size= 18)),
                              ft.Row(expand= 2, spacing= 5, alignment= ft.MainAxisAlignment.SPACE_AROUND,
                                     controls= [
                                        ft.ElevatedButton("Carrito", color= 'white', bgcolor= "#a10316", icon= ft.cupertino_icons.CART_BADGE_PLUS,
                                                      style= ft.ButtonStyle(overlay_color= {"hovered": '#db0616'},
                                                                     elevation= 200, shape= ft.RoundedRectangleBorder(radius= 20),
                                                                     side= ft.BorderSide(1, "#ffffff"))
                                          ),
                                        ft.ElevatedButton("Favoritos", color= 'white', bgcolor= "#a10316", icon= ft.icons.FAVORITE,
                                                      style= ft.ButtonStyle(overlay_color= {"hovered": '#db0616'},
                                                                     elevation= 200, shape= ft.RoundedRectangleBorder(radius= 20),
                                                                     side= ft.BorderSide(1, "#ffffff"))
                                          )
                                     ]),
                           ]
                        )
         ), 

      ]

   def close_view(self, e):
      self.page.views.pop()
      self.page.update()

class ProductCard(ft.Container):

   def __init__(self, page, title, description, img_src, price, rating, stock):
      super().__init__(
         alignment= ft.alignment.center,
         width= 150,
         height= 450,
         border_radius= 10,
         padding= 5,
         bgcolor= "#f2f2f2",
         )
      self.page = page
      self.title = title
      self.description = description
      self.img_src = img_src
      self.price = price
      self.rating = rating
      self.stock = stock

      #content of the class ProductCard
      self.content = ft.Column( expand= True,
                               controls=[
                                  ft.Stack(controls=[
                                     ft.Container(border_radius= 15, on_click= self.show_product, alignment= ft.alignment.center,
                                                  content= ft.Image(src= img_src, width= 120, height= 120, fit= 'cover')
                                       ),
                                       ft.Container(width= 60, alignment= ft.alignment.center, 
                                          border_radius= ft.border_radius.only(top_left= 10, bottom_right= 10),
                                          bgcolor= ft.colors.with_opacity(0.5, 'black'), 
                                          content= ft.Row(spacing= 5, controls=[
                                                      ft.Icon(name= ft.icons.STAR, color= ft.colors.YELLOW_100),
                                                      ft.Text(value= str(rating), weight= 'bold', color= ft.colors.YELLOW_400)
                                                      ]))
                                  ]),
                                  ft.Text(value= self.title, weight= 'bold'),
                                  ft.Text(value= self.description, color= ft.colors.BLACK87),
                                  ft.Row(alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                         controls= [
                                            ft.Text(spans= [
                                               ft.TextSpan(text= '$', style= ft.TextStyle(color= "#db0616")),
                                               ft.TextSpan(text= f'{price}', style= ft.TextStyle(color= ft.colors.BLACK)),
                                            ]),
                                            ft.IconButton(icon= ft.icons.ADD, icon_color= ft.colors.RED, on_click= self.add_cart)
                                         ])
                               ]
                     )
   
   def show_product(self, e):
      view = ProductView(self)
      self.page.views.append(view)
      self.page.update()
   
   def add_cart(self, e):
      print("añadido al carrito")
      pass
