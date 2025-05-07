import { Component, OnInit, OnDestroy } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-registrar',
  imports: [RouterModule],
  templateUrl: './registrar.component.html',
  styleUrl: './registrar.component.scss'
})

export class RegistrarComponent implements OnInit, OnDestroy {

  ngOnInit(): void {
    document.body.style.overflow = 'hidden';   // Remove scroll    
  }

  ngOnDestroy(): void {
    document.body.style.overflow = 'auto';     // Restaura scroll ao sair
  }
}