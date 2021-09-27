from HttpClient import HttpClient
from Matrix import Matrix
from sphere import Sphere

sphereVariable = Sphere()
print(sphereVariable.get_volume())
print(sphereVariable.get_square())
print(sphereVariable.get_radius())
print(sphereVariable.get_center())
print(sphereVariable.is_point_inside(0, 0, 0))


print("-- Matrix --")
matrix1 = Matrix([1, 2], [3, 2])
matrix2 = Matrix([1, 3], [3, 2])
print(matrix1 == matrix2)
print(matrix1 * matrix2)

print("-- HttpClient --")

client = HttpClient("https://httpbin.org")
client.set_header({"user-agent": "test_client"})
print(client.get(path="/get", query={"key_1":"value_1"}))
print(client.post(path="/status/400",query={"key_2":"value_2"}))