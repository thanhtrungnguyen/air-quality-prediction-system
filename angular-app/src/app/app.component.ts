import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AirQualityComponent } from "./pages/air-quality/air-quality.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, AirQualityComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Air Quality App';
}
