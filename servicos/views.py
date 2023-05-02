from django.shortcuts import render, get_object_or_404
from .forms import FormServico
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, FileResponse
from .models import Servico, CategoriaManutencao
from fpdf import FPDF   
from io import BytesIO

def servicos(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            form = FormServico()
            return render(request, 'servicos.html', {'form': form})
        else:
            return redirect(reverse('login'))

    elif request.method == "POST":
        form = FormServico(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Salvo com suceso!")
        else:
            return render(request, 'servicos.html', {'form': form})


def lista_servicos(request):
    if request.user.is_authenticated:
        servicos = Servico.objects.all()
        return render(request, 'lista_servicos.html', {'servicos': servicos})
    else:
            return redirect(reverse('login'))

def servico(request, identificador):
    if request.user.is_authenticated:
        servico = get_object_or_404(Servico, identificador=identificador)
        return render(request, 'servico.html', {'servico': servico})
    else:
            return redirect(reverse('login'))

def gerar_os(request, identificador):
    if request.user.is_authenticated:
        servico = get_object_or_404(Servico, identificador=identificador)
        
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font('Arial', 'B', 12)
        pdf.set_fill_color(240, 240, 240)

        pdf.cell(35, 10, 'Cliente:', 1, 0, 'L', 1)
        pdf.cell(0, 10, f'{servico.cliente.nome}', 1, 1, 'L', 1)

        pdf.cell(35, 10, 'Manutenções:', 1, 0, 'L', 1)
        categorias = servico.categoria.all()
        for i, manutencao in enumerate(categorias):
            pdf.cell(0, 10, f'- {manutencao.get_titulo_display()}', 1, 1, 'L', 1)
            if not i == len(categorias) - 1:
                pdf.cell(35, 10, '', 0, 0)

        pdf.cell(35, 10, 'Data de início:', 1, 0, 'L', 1)
        pdf.cell(0, 10, f'{servico.data_inicio}', 1, 1, 'L', 1)

        pdf.cell(35, 10, 'Data de entrega:', 1, 0, 'L', 1)
        pdf.cell(0, 10, f'{servico.data_entrega}', 1, 1, 'L', 1)

        pdf.cell(35, 10, 'Protocolo:', 1, 0, 'L', 1)
        pdf.cell(0, 10, f'{servico.protocolo}', 1, 1, 'L', 1)

        pdf.cell(35, 10, 'Preço total:', 1, 0, 'L', 1)
        pdf.cell(0, 10, f'{servico.preco_total()}', 1, 1, 'L', 1)

        
        pdf_content = pdf.output(dest='S').encode('latin1')
        pdf_bytes = BytesIO(pdf_content)

        return FileResponse(pdf_bytes, as_attachment=True, filename="os.pdf")
    
    else:
            return redirect(reverse('login'))


