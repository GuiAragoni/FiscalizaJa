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


// export class RegistrarComponent implements OnInit, OnDestroy {

export class RegistrarComponent {
  nome = '';
  email = '';
  senha = '';
  confirmarSenha = '';

  constructor(private cidadaoService: CidadaoService) {}


    registrarCidadao() {
    if (this.senha !== this.confirmarSenha) {
      alert('As senhas não coincidem!');
      return;
    }


     const novoCidadao = {
      Nome: this.nome,
      Email: this.email,
      Senha: this.senha
    };

    this.cidadaoService.registrarCidadao(novoCidadao).subscribe({
      next: () => alert('Usuário registrado com sucesso!'),
      error: (err) => alert('Erro ao registrar: ' + err.error?.erro)
    });
  }


  ngOnInit(): void {
    document.body.style.overflow = 'hidden';   // Remove scroll    
  }

  ngOnDestroy(): void {
    document.body.style.overflow = 'auto';     // Restaura scroll ao sair
  }
  }
