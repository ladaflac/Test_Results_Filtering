from django.shortcuts import render
import Generate_Table


def index(request):
    results_table = Generate_Table.main()
    return render(request, 'filteringapp/index.html', context={"results": results_table})
