import { Component, OnInit, OnDestroy } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule }   from '@angular/common';
import { FormsModule }    from '@angular/forms';
import { CidadaoService } from '../../services/cidadao.service';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-registrar',
  standalone: true,
  imports: [
    CommonModule,       
    FormsModule,        
    RouterModule
  ],
  templateUrl: './registrar.component.html',
  styleUrls:   ['./registrar.component.scss']
})

export class RegistrarComponent implements OnInit, OnDestroy {

  nome = '';
  email = '';
  senha = '';
  confirmarSenha = '';
  cpf = '';
  telefone = '';
  endereco = '';

  estadoSelecionado = '';
  cidadeSelecionada = '';

  estados: any[] = [];
  cidades: any[] = [];

  constructor(
    private cidadaoService: CidadaoService,
    private http: HttpClient
  ) {}

  ngOnInit(): void {
    document.body.style.overflow = 'hidden';

    // Carrega os estados ao abrir a tela
    this.http.get<any[]>('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
      .subscribe(res => {
        this.estados = res.sort((a, b) => a.nome.localeCompare(b.nome));
      });
  }

  onEstadoChange() {
    if (this.estadoSelecionado) {
      this.http.get<any[]>(`https://servicodados.ibge.gov.br/api/v1/localidades/estados/${this.estadoSelecionado}/municipios`)
        .subscribe(res => {
          this.cidades = res.sort((a, b) => a.nome.localeCompare(b.nome));
        });
    } else {
      this.cidades = [];
    }
  }

  registrarCidadao() {
    debugger

    if (this.estadoSelecionado == "" || this.cidadeSelecionada == "") {
      alert('Selecionar um Estado e uma Cidade!');
      return;
    }

    if (this.senha !== this.confirmarSenha) {
      alert('As senhas não coincidem!');
      return;
    }

    const novoCidadao = {
      Nome: this.nome,
      Email: this.email,
      Senha: this.senha,
      Cpf: this.cpf,
      Telefone: this.telefone,
      Estado: this.estadoSelecionado,
      Cidade: this.cidadeSelecionada
    };

    this.cidadaoService.registrarCidadao(novoCidadao).subscribe({
      next: () => alert('Usuário registrado com sucesso!'),
      error: (err) => alert('Erro ao registrar: ' + err.error?.erro)
    });
  }

  ngOnDestroy(): void {
    document.body.style.overflow = 'auto';
  }
}