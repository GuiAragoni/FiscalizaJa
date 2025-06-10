import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavbarComponent } from './components/navbar/navbar.component';
import { HomeComponent } from './components/home/home.component';
import { RegistrarComponent } from './components/registrar/registrar.component';
import { LoginComponent } from './components/login/login.component';
import { Router, NavigationEnd } from '@angular/router';
import { SobreNosComponent } from './components/sobre-nos/sobre-nos.component';
import { CentralAjudaComponent } from './components/central-ajuda/central-ajuda.component';
import { PoliticaPrivacidadeComponent } from './components/politica-privacidade/politica-privacidade.component';


@Component({
  selector: 'app-root',
  imports: [RouterOutlet, NavbarComponent, HomeComponent, RegistrarComponent,LoginComponent, SobreNosComponent, CentralAjudaComponent, PoliticaPrivacidadeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})

export class AppComponent {
  constructor(private router: Router) {
    // Sempre rola para o topo após a navegação
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        window.scrollTo(0, 0);
      }
    });
  }
}