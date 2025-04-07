from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ENQUIRY.forms import StudentEnquiryForm
from ENQUIRY.models import StudentEnquiry
from ENQUIRY.serializers import StudentEnquirySerializer


# -----------------------------
# ✅ Template-Based Views (use ModelForm)
# -----------------------------
def student_list(request):
    students = StudentEnquiry.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        form = StudentEnquiryForm(request.POST)
        if form.is_valid():
            # Do extra validation via serializer
            serializer = StudentEnquirySerializer(data=form.cleaned_data)
            if serializer.is_valid():
                serializer.save()
                return redirect('student_list')
            else:
                # Push serializer errors back into form
                for field, errors in serializer.errors.items():
                    for error in errors:
                        form.add_error(field, error)
        # Form has errors or serializer failed
        return render(request, 'student_create.html', {'form': form})
    
    form = StudentEnquiryForm()
    return render(request, 'student_create.html', {'form': form})


def student_detail(request, pk):
    student = get_object_or_404(StudentEnquiry, pk=pk)
    return render(request, 'student_detail.html', {'student': student})


# -----------------------------
# ✅ API ViewSet (use DRF Serializers)
# -----------------------------
class StudentEnquiryViewSet(viewsets.ModelViewSet):
    queryset = StudentEnquiry.objects.all()
    serializer_class = StudentEnquirySerializer

    def create(self, request):
        serializer = StudentEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'StudentEnquiry inserted successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        student_enquiry = get_object_or_404(StudentEnquiry, pk=pk)
        serializer = StudentEnquirySerializer(student_enquiry)
        return Response(serializer.data)

    def list(self, request):
        student_enquiries = StudentEnquiry.objects.all()
        serializer = StudentEnquirySerializer(student_enquiries, many=True)
        return Response({
            'count': student_enquiries.count(),
            'data': serializer.data
        })

    def update(self, request, pk=None):
        student_enquiry = get_object_or_404(StudentEnquiry, pk=pk)
        serializer = StudentEnquirySerializer(student_enquiry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'StudentEnquiry updated successfully',
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student_enquiry = get_object_or_404(StudentEnquiry, pk=pk)
        student_enquiry.delete()
        return Response({'message': 'StudentEnquiry deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def get_by_course(self, request):
        course = request.query_params.get('course')
        if not course:
            return Response({'error': 'Course parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        student_enquiries = StudentEnquiry.objects.filter(course__icontains=course)
        serializer = StudentEnquirySerializer(student_enquiries, many=True)
        return Response({
            'count': student_enquiries.count(),
            'data': serializer.data
        })
