import { CommonModule } from '@angular/common';
import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule,Validators } from '@angular/forms';
import { PlayerService } from '../Services/player.service';
import { HttpClientModule } from '@angular/common/http';
import { Player } from '../../models/player.models';

@Component({
  selector: 'app-playerui',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, HttpClientModule, FormsModule],
  templateUrl: './playerui.component.html',
  styleUrls: ['./playerui.component.css'],
  providers: [PlayerService]
})
export class PlayeruiComponent implements OnInit {
  add_player_bool: boolean = false;
  myForm: FormGroup;
  editForm: FormGroup;
  display_check: boolean = false;
  ascending: boolean = false;
  player_list: Player[] = [];
  sort: boolean = false;
  all_checked: boolean = false;
  edit_player_roll: any;
  open: boolean = false;
  actionType: string;
  edit_player_id: number = 0;
  sort_using: string = '';
  sortedData: Player[] = [];
  text_search=''
  next_number:number=0


  constructor(private fb: FormBuilder, public playerService: PlayerService, private cdr: ChangeDetectorRef) {
    this.myForm = this.fb.group({
      player_no: [''],
      name: ['',[Validators.required,Validators.minLength(3)]],
      age: ['',[Validators.required, Validators.min(1), Validators.max(100) ]],
      batting_rating: ['',[Validators.required, Validators.min(1), Validators.max(10)]],
      bowling_rating: ['',[Validators.required, Validators.min(1), Validators.max(10)]],
      wicket_keeper_rating: ['',[Validators.required, Validators.min(1), Validators.max(10)]]
    });

    this.editForm = this.fb.group({
      player_no: [''],
      name: [''],
      age: [''],
      batting_rating: [''],
      bowling_rating: [''],
      wicket_keeper_rating: ['']
    });

    this.actionType = '';
  }

  setAction(action: string) {
    this.actionType = action;
  }

  add_player_check() {
    this.next_number=(this.player_list.reduce((max, player) => player.player_no > max ? player.player_no : max, 0)+1)
    if (this.edit_player_roll != null) {
      this.cancel_edit();
    } else {
      this.add_player_bool = !this.add_player_bool;
      this.resetForm();
      console.log(this.add_player_bool);
    }
  }

  get_all_players() {
    this.playerService.getPlayers().subscribe((response) => {
      this.player_list = response.sort((a: any, b: any) => b.player_no - a.player_no);
      this.applySort(); // Apply sorting after fetching data
      this.cdr.detectChanges();
      return this.player_list;
    });
  }

  ngOnInit() {
    this.get_all_players()
    console.log(this.player_list.length)
    
  }

  resetForm() {
    this.myForm.reset();
    this.editForm.reset();
  }

  onSubmit(): void {
    if (this.myForm.invalid) {
      // If the form is invalid, mark all fields as touched to trigger validation messages
      this.myForm.markAllAsTouched();
      return;
    }
    if (this.add_player_bool) {
      // Find the highest player number in the original player list
      const highestPlayerNo = this.player_list.reduce((max, player) => player.player_no > max ? player.player_no : max, 0);
      const newPlayerNo = highestPlayerNo + 1;
      this.myForm.value['player_no'] = newPlayerNo;
  
      this.playerService.add_players(this.myForm.value).subscribe((response) => {
        this.get_all_players();
        this.resetForm();
        console.log(response);
      });
    } else if (this.edit_player_roll != null) {
      this.myForm.value['player_no'] = this.edit_player_roll;
      this.playerService.add_players(this.myForm.value).subscribe((response) => {
        this.get_all_players();
        this.cancel_edit();
        console.log(response);
      });
    }
  }

  needToSort(col_sort: any) {
    this.sort_using = col_sort;
    this.sort = true;
    this.ascending = !this.ascending;
    this.applySort();
    this.cdr.detectChanges();
  }

  applySort() {
    if (this.sort_using === 'name') {
      this.sortedData = this.player_list.sort((a: any, b: any) =>
        this.ascending ? a.name.localeCompare(b.name) : b.name.localeCompare(a.name)
      );
    } else if (this.sort_using === 'age') {
      this.sortedData = this.player_list.sort((a: any, b: any) =>
        this.ascending ? a.age - b.age : b.age - a.age
      );
    } else if (this.sort_using === 'batting_rating') {
      this.sortedData = this.player_list.sort((a: any, b: any) =>
        this.ascending ? a.batting_rating - b.batting_rating : b.batting_rating - a.batting_rating
      );
    } else if (this.sort_using === 'bowling_rating') {
      this.sortedData = this.player_list.sort((a: any, b: any) =>
        this.ascending ? a.bowling_rating - b.bowling_rating : b.bowling_rating - a.bowling_rating
      );
    } else if (this.sort_using === 'wicket_keeper_rating') {
      this.sortedData = this.player_list.sort((a: any, b: any) =>
        this.ascending ? a.wicket_keeper_rating - b.wicket_keeper_rating : b.wicket_keeper_rating - a.wicket_keeper_rating
      );
    }
  }

  checkAll() {
    this.all_checked = !this.all_checked;
  }

  selected_data: any[] = [];
  delete_selected(player_no: any) {
    this.selected_data.push(player_no);
  }

  delete_all: boolean = false;
  delete_selected_all(selected_data: any) {
    if (this.all_checked) {
      this.playerService.delete_all_data().subscribe((response) => {
        this.display_check = true;
        this.get_all_players();
      });
    } else {
      this.playerService.delete_selected(selected_data).subscribe((response) => {
        console.log(response);
        this.get_all_players();
      });
    }
  }

  delete_sort: boolean = false;
  delete_record(id: number) {
    this.playerService.delete_player_info(id).subscribe((response) => {
      this.get_all_players();
      if (this.sort) {
        this.applySort();
      }
      this.cdr.detectChanges();
    });
  }

  single_player_info: any;
  find_one_player(id: any) {
    this.playerService.single_player(id).subscribe((response) => {
      this.single_player_info = response;
      console.log(response);
    });
  }

  cancel_edit() {
    this.edit_player_roll = null;
  }

  single_data: any;
  edit_player_info(id: any) {
    this.edit_player_roll = id;
    if (this.add_player_bool) this.add_player_check();
    this.playerService.single_player(id).subscribe((response) => {
      this.single_data = response;
      // this.cdr.detectChanges();
    });
  }

  save_edit: boolean = false;
  save_edit_data() {
    this.save_edit = !this.save_edit;
  }

  updated_player_info() {
    console.log(this.editForm.value);
  }

  
  // checkValidLetters(letters:any){
   
  //   else if (letters.keyCode >= 65 && letters.keyCode <= 90){
      
  //     this.text_search+=letters.key
  //     this.getPlayerSearch(this.text_search)
  //   }
    
  // }
  filered_data:any=[]
  getPlayerSearch(text:any){
    console.log(text)
    var filterData=this.player_list.filter((item) =>
      item.name.toLowerCase().includes(text.toLowerCase())
    )
    this.filered_data=filterData
    
  }
  
  search:boolean=false
  handleKeyDown(pressedKey:any){
    this.search=true
    if (pressedKey.keyCode==8){
      //console.log(pressedKey.keyCode)
      this.text_search=this.text_search.slice(0,-1)
      console.log(this.text_search)
      this.getPlayerSearch(this.text_search)
      
    }
    else if (pressedKey.keyCode >= 65 && pressedKey.keyCode <= 90){
      
        this.text_search+=pressedKey.key
        this.getPlayerSearch(this.text_search)
    }
    if (this.text_search.length==0){
        this.search=false
      }
      console.log(this.search)
  }
}
