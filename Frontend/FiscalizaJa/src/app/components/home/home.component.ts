import { Component, AfterViewInit, OnDestroy } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-home',  
  imports: [RouterModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements AfterViewInit, OnDestroy {

  private scrollHandler = () => {
    const footer = document.getElementById('footer');
    if (!footer) return;

    const footerBottom = footer.getBoundingClientRect().bottom + window.scrollY;
    const maxScroll = footerBottom - window.innerHeight;

    if (window.scrollY > maxScroll) {
      window.scrollTo({ top: maxScroll });
    }
  };

  ngAfterViewInit(): void {
    window.addEventListener('scroll', this.scrollHandler);
  }

  ngOnDestroy(): void {
    window.removeEventListener('scroll', this.scrollHandler);
  }
}
