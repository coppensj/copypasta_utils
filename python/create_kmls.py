import simplekml

def AddLocations(kml_doc, locations, name, point_radius=100):
    style = simplekml.Style()
    style.labelstyle.color = simplekml.Color.black  # Make the text black
    style.labelstyle.scale = 0.5  # Make the text half as big
    style.iconstyle.icon.href = "http://maps.google.com/mapfiles/kml/paddle/red-circle.png"
    for point in locations:
        pnt = kml_doc.newpoint(name=name)
        pnt.coords = [(point[0], point[1])]
        pnt.style = style

def AddPolygons(kml_doc, polygons, name):
    style = simplekml.Style()
    style.linestyle.color = simplekml.Color.black
    style.linestyle.width = 4
    style.polystyle.outline = 1
    style.polystyle.color = simplekml.Color.changealphaint(0, simplekml.Color.red)
    
    for polygon in polygons:
        poly = kml_doc.newpolygon(outerboundaryis=polygon) 
        poly.name = name
        poly.style = style

if __name__ == "__main__":
    coords = [(-118.4063, 33.906), (-118.287, 33.777), 
        (-118.2277, 33.8892)]
    
    polygons = [[(-118.4063, 33.906), (-118.287, 33.777), 
        (-118.2277, 33.8892), (-118.4063, 33.906)]]

    doc = simplekml.Kml(open=1)
    AddLocations(doc, coords, "Test", point_radius=500)
    AddPolygons(doc, polygons, "Test Polygon")
    doc.save(f"test_kml.kml")
