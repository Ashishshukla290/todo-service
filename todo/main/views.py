from rest_framework.response import Response
from rest_framework import viewsets
from .models import Todo
from .serializer import TodoSerializer
from rest_framework import status


class Todoviewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def readtask(self, request, id):
        try:
            res = self.queryset.filter(task_id=id).first()
            ser = self.get_serializer(res).data
            res = {}
            res["res"] = ser
            return Response(res)
        except Exception as e:
            return Response(str(e))

    def readall(self, request):
        st = self.get_serializer(self.queryset, many=True)
        res = {}
        res["ans"] = st.data
        return Response(res)

    def change(self, request, id):
        try:
            res = self.queryset.filter(task_id=id).first()
            ser = self.get_serializer(res, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        except Exception as e:
            return Response(str(e))

    def destroy(self, request, id):
        try:
            res = self.queryset.filter(task_id=id).first()
            res.delete()
            return Response({"message": "Deleted"})
        except Exception as e:
            return Response(str(e))
