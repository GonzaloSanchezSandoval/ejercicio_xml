from lxml import etree

libros = etree.parse("Proyecto_2ºEvaluación_Autor.xml")


def listar_libros(libros):
    lista_libros=libros.xpath("/Sanderson_Books/Cosmere/book/@titulo")
    return(lista_libros)

def contar_premios(libros):
    lista_premios=libros.xpath("/Sanderson_Books/biography/awards/award/title/text()")
    return(len(lista_premios))

def filtrar_nombre(libros, nombre):
        lista_libros=[]
        if nombre in libros.xpath("/Sanderson_Books/Cosmere/book/Characters/text()"):
            lista_libros.append(libros.xpath("/Sanderson_Books/Cosmere/book/titulo/text()"))
        
        if nombre in libros.xpath("/Sanderson_Books/Non_Cosmere/The_Reckoners/book/Characters/text()"):
            lista_libros.append(libros.xpath("/Sanderson_Books/Cosmere/book/titulo/text()"))

            
        return listar_libros