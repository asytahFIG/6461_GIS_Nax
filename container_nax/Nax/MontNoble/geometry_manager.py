from shapely.geometry import Polygon
import shapely.wkt


def load_shapely_from_geodjango(geoDjangoModel):
      # The ; is the delimiter before the start of the geodjango
      return shapely.wkt.loads(str(geoDjangoModel.geom).partition(";")[2])

def is_neighbor_intersect(model, other):
      model_polygon = load_shapely_from_geodjango(model)
      other_polygon = load_shapely_from_geodjango(other)
      
      # Using minimal distance
      if (model_polygon.intersects(other_polygon) or model_polygon.distance(other_polygon) <= 50):
            return True
      return False

def get_list_of_neighbors_intersect(model, others_list):
      neighbors = []
      for other in others_list:
            if (is_neighbor_intersect(model, other)):
                  neighbors.append(other)

      return neighbors

def get_list_of_neighbors_crosses(model, others_list):
      neighbors = []
      for other in others_list:
            if (is_neighbor_crosses(model, other)):
                  neighbors.append(other)

      return neighbors

def is_neighbor_crosses(model, other):
      model_polygon = load_shapely_from_geodjango(model)
      other_polygon = load_shapely_from_geodjango(other)
      
      # Using crossing
      if (model_polygon.crosses(other_polygon)):
            return True
      return False