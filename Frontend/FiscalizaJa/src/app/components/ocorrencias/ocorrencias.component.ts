import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-ocorrencias',
  standalone: true,  
  imports: [
    CommonModule,       
    FormsModule,        
    RouterModule
  ],
  templateUrl: './ocorrencias.component.html',
  styleUrl: './ocorrencias.component.scss',
})
export class OcorrenciasComponent {

}
