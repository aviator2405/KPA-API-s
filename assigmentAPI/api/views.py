from rest_framework import generics, filters, status
from rest_framework.response import Response
from application.models import WheelSpecification
from application.serializers import WheelSpecificationSerializer

class WheelSpecificationView(generics.ListCreateAPIView):
    queryset = WheelSpecification.objects.all()
    serializer_class = WheelSpecificationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['formNumber', 'submittedBy', 'submittedDate']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data = serializer.data
        custom_response = {
            "success": True,
            "message": "Wheel specification submitted successfully.",
            "data": {
                "formNumber": data.get("formNumber"),
                "submittedBy": data.get("submittedBy"),
                "submittedDate": data.get("submittedDate"),
                "status": "Saved"
            }
        }
        return Response(custom_response, status=status.HTTP_201_CREATED)

class WheelSpecificationFilterView(generics.ListAPIView):
    serializer_class = WheelSpecificationSerializer

    def get_queryset(self):
        queryset = WheelSpecification.objects.all()
        form_number = self.request.query_params.get('form_number')
        submitted_by = self.request.query_params.get('submitted_by')
        submitted_date = self.request.query_params.get('submitted_date')
        # print(form_number)

        if form_number:
            queryset = queryset.filter(form_number=form_number)
        if submitted_by:
            queryset = queryset.filter(submitted_by=submitted_by)
        if submitted_date:
            queryset = queryset.filter(submitted_date=submitted_date)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        })