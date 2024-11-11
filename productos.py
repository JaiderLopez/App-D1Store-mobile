import flet as ft

class ProductView(ft.View):
   def __init__(self, product):
      super().__init__(bgcolor= ft.colors.TRANSPARENT)
      self.product = product
      
      self.controls = [
         ft.Container(expand=True, alignment= ft.alignment.center, bgcolor= "#0b0e13",
                      margin= 10,
                      content= ft.Column(expand= True, horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                         controls= [
                                            ft.Stack(expand= 8, 
                                                     controls=[
                                                        ft.Container(alignment= ft.alignment.center, border_radius= 20,
                                                                  content= ft.Image(src= self.product.img_src, width= 300,
                                                                                    height= 400, fit= 'cover')),
                                                         ft.Container(content=ft.Row([ft.Icon(name= ft.icons.KEYBOARD_ARROW_LEFT),
                                                                 ft.Text("Volver", color= 'white')]), on_click= self.close_view)
                                                     ]),
                                          
                                         ]
                              )
         )
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
