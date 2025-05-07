import { Component , OnInit, OnDestroy } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-login',
  imports: [RouterModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent implements OnInit, OnDestroy {

  ngOnInit(): void {
    document.body.style.overflow = 'hidden';   // Remove scroll
  }

  ngOnDestroy(): void {
    document.body.style.overflow = 'auto';     // Restaura scroll ao sair
  }
}