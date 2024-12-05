import { Component } from '@angular/core';
import { AirQualityDetailComponent } from './components/air-quality-detail/air-quality-detail.component';
import { AirQualityForecastComponent } from './components/air-quality-forecast/air-quality-forecast.component';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  // standalone: true,
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'Air quality predictions';
}
