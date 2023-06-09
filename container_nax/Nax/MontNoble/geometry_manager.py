from shapely.geometry import Polygon
import shapely.wkt


def load_shapely_from_geodjango(geoDjangoModel):
      return shapely.wkt.loads(str(geoDjangoModel.geom).partition(";")[2])



