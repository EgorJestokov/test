from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .models import CreateProduct, CreatePrice, CreateSale
from .forms import formProduct, formPrice, formSales
from django.views.generic import UpdateView, DeleteView
from django.core.paginator import Paginator


# создание и сохранение записи
# @login_required(login_url='/login')
# def create_and_save(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     if request.method == "POST":
#         form = CreateItem(request.POST)
#         if form.is_valid():
#             form.save()
#     form = CreateItem()
#     context = {'form': form}
#     return render(request, 'manual/index.html', context)


#Блок кода для справочника услуг и товаров

def mainProduct(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = CreateProduct.objects.order_by('-date')
    #Пагинация
    reports = CreateProduct.objects.order_by('-date')
    per_page = 8
    p = Paginator(reports, per_page)
    page = request.GET.get('page')
    items = p.get_page(page)

    # if request.method == "POST":
    #     form = formProduct(request.POST)
    #     if form.is_valid():
    #         form.save()
    # form = formProduct()
    context = {'posts': posts, 'items': items}
    return render(request,'manual/product_manual.html', context)


@login_required(login_url='/login')
def createProduct(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = formProduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-product')
    CreateProduct.objects.all().order_by('-date')
    form = formProduct()
    context = {'form': form}
    return render(request, 'manual/create_product.html', context)


@login_required(login_url='/login')
def editProduct(request, pk):
    post = CreateProduct.objects.get(id=pk)
    form = formProduct(instance=post)

    if request.method == 'POST':
        form = formProduct(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('main-product')

    context = {'form': form}
    return render(request, 'manual/edit_product.html', context)


@login_required(login_url='/login')
def deleteProduct(request, pk):
    post = CreateProduct.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('main-product')
    return render(request, 'manual/delete_product.html', {'obj': post})


def sortProductDate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = CreateProduct.objects.order_by('-date')
    #Пагинация
    reports = CreateProduct.objects.order_by('-date')
    per_page = 8
    p = Paginator(reports, per_page)
    page = request.GET.get('page')
    items = p.get_page(page)

    # if request.method == "POST":
    #     form = formProduct(request.POST)
    #     if form.is_valid():
    #         form.save()
    # form = formProduct()
    context = {'posts': posts, 'items': items}
    return render(request,'manual/product_manual.html', context)


def sortProductDefault(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = CreateProduct.objects.all()
    #Пагинация
    reports = CreateProduct.objects.all()
    per_page = 8
    p = Paginator(reports, per_page)
    page = request.GET.get('page')
    items = p.get_page(page)

    # if request.method == "POST":
    #     form = formProduct(request.POST)
    #     if form.is_valid():
    #         form.save()
    # form = formProduct()
    context = {'posts': posts, 'items': items}
    return render(request,'manual/product_manual.html', context)

#Блок кода для справочника цен

@login_required(login_url='/login')
def mainPrice(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = CreatePrice.objects.all()
    #Пагинация
    reports = CreatePrice.objects.all()
    per_page = 8
    p = Paginator(reports, per_page)
    page = request.GET.get('page')
    items = p.get_page(page)
    # if request.method == "POST":
    #     form = formPrice(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('main-price')
    # form = formPrice()
    # context = {'posts': posts, 'items': items}
    context = {'posts': posts, 'items': items}
    return render(request, 'manual/price_manual.html', context)


@login_required(login_url='/login')
def createPrice(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = formPrice(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-price')
    form = formPrice()
    context = {'form': form}
    return render(request, 'manual/create_price.html', context)


@login_required(login_url='/login')
def editPrice(request, pk):
    post = CreatePrice.objects.get(id=pk)
    form = formPrice(instance=post)

    if request.method == 'POST':
        form = formPrice(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('main-price')

    context = {'form': form}
    return render(request, 'manual/edit_product.html', context)



@login_required(login_url='/login')
def deletePrice(request, pk):
    post = CreatePrice.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('main-price')
    return render(request, 'manual/delete_product.html', {'obj': post})



# Открытие списка с отчетом
@login_required(login_url='/login')
def report(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = CreateProduct.objects.all()

    #Пагинация
    reports = CreateProduct.objects.all()
    per_page = 8
    p = Paginator(reports, per_page)
    page = request.GET.get('page')
    items = p.get_page(page)

    context = {'posts': posts, 'items': items}
    return render(request,'manual/report.html', context)


# Сохранение записи в справочник объема продаж
@login_required(login_url='/login')
def mainSale(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = formSales(request.POST)
        if form.is_valid():
            form.save()
            redirect('main-sale')
    reports = CreateSale.objects.all()
    per_page = 8
    p = Paginator(reports, per_page)
    page = request.GET.get('page')
    items = p.get_page(page)
    form = formSales()
    context = {'form': form, 'report': reports, 'items': items}
    return render(request, 'manual/sale_manual.html', context)


@login_required(login_url='/login')
def createSale(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = formSales(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-sale')
    form = formSales()
    context = {'form': form}
    return render(request, 'manual/create_sale.html', context)


@login_required(login_url='/login')
def editSale(request, pk):
    post = CreateSale.objects.get(id=pk)
    form = formSales(instance=post)

    if request.method == 'POST':
        form = formSales(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('main-sale')

    context = {'form': form}
    return render(request, 'manual/edit_sale.html', context)

@login_required(login_url='/login')
def deleteSale(request, pk):
    post = CreateSale.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('main-sale')
    return render(request, 'manual/delete_sale.html', {'obj': post})



def createManual(request):
    return render(request, 'manual/create_manual.html')
