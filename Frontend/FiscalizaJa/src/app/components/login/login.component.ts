import { Component , OnInit, OnDestroy } from '@angular/core';
import { CidadaoService } from '../../services/cidadao.service';
import { RouterModule } from '@angular/router';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  imports: [CommonModule,RouterModule,FormsModule],
  standalone: true,
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent implements OnInit, OnDestroy {

cpfEmail = '';
senha = '';  

//constructor(private cidadaoService: CidadaoService) {}
constructor(private cidadaoService: CidadaoService, private router: Router) {}


login() {
  debugger
  this.cidadaoService.loginCidadao(this.cpfEmail).subscribe({
    next: (cidadao) => {
      if (cidadao.Senha === this.senha) {
        alert('Login APROVADO');
        //this.router.navigate(['/home']);
      } else {
        alert('Senha incorreta.');
      }
    },
    error: () => {
      alert('Usuário não encontrado.');
    }
  });
}

  ngOnInit(): void {
    document.body.style.overflow = 'hidden';   // Remove scroll
  }

  ngOnDestroy(): void {
    document.body.style.overflow = 'auto';     // Restaura scroll ao sair
  }
}