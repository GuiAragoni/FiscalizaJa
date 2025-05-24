import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { RegistrarComponent } from './components/registrar/registrar.component';
import { LoginComponent } from './components/login/login.component';
import { SobreNosComponent } from './components/sobre-nos/sobre-nos.component';
import { CentralAjudaComponent } from './components/central-ajuda/central-ajuda.component';
import { PoliticaPrivacidadeComponent } from './components/politica-privacidade/politica-privacidade.component';

export const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'registrar', component: RegistrarComponent },
  { path: 'login', component: LoginComponent },  
  { path: 'sobre-nos', component: SobreNosComponent },  
  { path: 'central-ajuda', component: CentralAjudaComponent },  
  { path: 'politica-privacidade', component: PoliticaPrivacidadeComponent },  
];
