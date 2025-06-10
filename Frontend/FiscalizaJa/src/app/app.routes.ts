import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { RegistrarComponent } from './components/registrar/registrar.component';
import { LoginComponent } from './components/login/login.component';
import { SobreNosComponent } from './components/sobre-nos/sobre-nos.component';
import { CentralAjudaComponent } from './components/central-ajuda/central-ajuda.component';
import { PoliticaPrivacidadeComponent } from './components/politica-privacidade/politica-privacidade.component';
import { OcorrenciasComponent } from './components/ocorrencias/ocorrencias.component';
import { DescricaoOcorrenciaComponent } from './components/descricao-ocorrencia/descricao-ocorrencia.component';
import { UsuarioHomeComponent } from './components/usuario-home/usuario-home.component';
import { SecretariaHomeComponent } from './components/secretaria-home/secretaria-home.component';

export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'registrar', component: RegistrarComponent },
  { path: 'login', component: LoginComponent },  
  { path: 'sobre-nos', component: SobreNosComponent },          
  { path: 'ocorrencias', component: OcorrenciasComponent },      
  { path: 'central-ajuda', component: CentralAjudaComponent },
  { path: 'descricao-ocorrencia', component: DescricaoOcorrenciaComponent },
  { path: 'usuario-home', component: UsuarioHomeComponent },
  { path: 'secretaria-home', component: SecretariaHomeComponent },
  { path: 'politica-privacidade', component: PoliticaPrivacidadeComponent },    
];
