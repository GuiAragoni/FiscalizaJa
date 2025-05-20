import { Component, OnInit, OnDestroy } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule }   from '@angular/common';
import { FormsModule }    from '@angular/forms';
import { CidadaoService } from '../../services/cidadao.service';
import { Router } from '@angular/router';



@Component({
  selector: 'app-registrar',
  standalone: true,
  imports: [
    CommonModule,       // para diretivas estruturais
    FormsModule,        // para [(ngModel)]
    RouterModule
  ],
  templateUrl: './registrar.component.html',
  styleUrls:   ['./registrar.component.scss']
})


export class RegistrarComponent implements OnInit, OnDestroy {

  nome = ''; email = ''; telefone = ''; cpf = ''; endereco = '';

  constructor(private svc: CidadaoService, private router: Router) {}

  registrar() {
    this.svc.criar({
      Nome: this.nome,
      Email: this.email,
      Telefone: this.telefone,
      CPF: this.cpf,
      Endereco: this.endereco
    }).subscribe({
      next: () => {
        alert('Registrado!');
        this.router.navigate(['/login']);
      },
      error: e => alert('Erro: ' + e.error?.erro)
    });
  }


  ngOnInit(): void {
    document.body.style.overflow = 'hidden';   // Remove scroll    
  }

  ngOnDestroy(): void {
    document.body.style.overflow = 'auto';     // Restaura scroll ao sair
  }
}