import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { RegistrarComponent } from './components/registrar/registrar.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'registrar', component: RegistrarComponent },  
];
