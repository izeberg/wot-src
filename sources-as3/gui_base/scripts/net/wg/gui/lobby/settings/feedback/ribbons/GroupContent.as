package net.wg.gui.lobby.settings.feedback.ribbons
{
   import flash.display.DisplayObject;
   import flash.events.Event;
   import net.wg.gui.components.controls.CheckBox;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.core.UIComponent;
   
   public class GroupContent extends UIComponent
   {
      
      private static const CHECK_BOX_TEXT_LINE_SPACING:Number = 2;
       
      
      private var _allItems:Array;
      
      private var _itemsOffsetsList:Array;
      
      public function GroupContent()
      {
         super();
      }
      
      public function set isEnabled(param1:Boolean) : void
      {
         var _loc2_:CheckBox = null;
         var _loc3_:int = 0;
         while(_loc3_ < this.numChildren)
         {
            _loc2_ = this.getChildAt(_loc3_) as CheckBox;
            if(_loc2_)
            {
               _loc2_.enabled = param1;
            }
            _loc3_++;
         }
      }
      
      override protected function onDispose() : void
      {
         this._allItems = null;
         this._itemsOffsetsList = null;
         super.onDispose();
      }
      
      public function get isSelectedAnyCheckbox() : Boolean
      {
         var _loc1_:CheckBox = null;
         var _loc2_:int = 0;
         while(_loc2_ < this.numChildren)
         {
            _loc1_ = this.getChildAt(_loc2_) as CheckBox;
            if(_loc1_ && _loc1_.selected)
            {
               return true;
            }
            _loc2_++;
         }
         return false;
      }
      
      public function get selectedItemsAmount() : int
      {
         var _loc2_:CheckBox = null;
         var _loc1_:int = 0;
         var _loc3_:int = 0;
         while(_loc3_ < this.numChildren)
         {
            _loc2_ = this.getChildAt(_loc3_) as CheckBox;
            if(_loc2_ && _loc2_.selected)
            {
               _loc1_++;
            }
            _loc3_++;
         }
         return _loc1_;
      }
      
      public function selectAllCheckBoxes() : void
      {
         var _loc1_:CheckBox = null;
         var _loc2_:int = 0;
         while(_loc2_ < this.numChildren)
         {
            _loc1_ = this.getChildAt(_loc2_) as CheckBox;
            if(_loc1_)
            {
               _loc1_.selected = true;
            }
            _loc2_++;
         }
      }
      
      override protected function initialize() : void
      {
         var _loc2_:DisplayObject = null;
         this._allItems = [];
         var _loc1_:int = 0;
         while(_loc1_ < this.numChildren)
         {
            this._allItems[this._allItems.length] = this.getChildAt(_loc1_);
            _loc1_++;
         }
         this._allItems.sortOn("y",Array.NUMERIC);
         this._itemsOffsetsList = [];
         var _loc3_:DisplayObject = this._allItems[0];
         var _loc4_:uint = this._allItems.length;
         _loc1_ = 1;
         while(_loc1_ < _loc4_)
         {
            _loc2_ = this._allItems[_loc1_];
            this._itemsOffsetsList[this._itemsOffsetsList.length] = _loc2_.y - _loc3_.y - _loc3_.height;
            _loc3_ = _loc2_;
            _loc1_++;
         }
         super.initialize();
      }
      
      override protected function configUI() : void
      {
         var _loc1_:DisplayObject = null;
         super.configUI();
         var _loc2_:int = 0;
         while(_loc2_ < this.numChildren)
         {
            _loc1_ = this.getChildAt(_loc2_);
            if(_loc1_ is CheckBox)
            {
               CheckBox(_loc1_).multiline = true;
               CheckBox(_loc1_).wordWrap = true;
               CheckBox(_loc1_).textLineSpacing = CHECK_BOX_TEXT_LINE_SPACING;
            }
            _loc1_.addEventListener(Event.RENDER,this.renderHandler);
            _loc2_++;
         }
      }
      
      override protected function draw() : void
      {
         var _loc1_:DisplayObject = null;
         var _loc2_:DisplayObject = null;
         var _loc3_:uint = 0;
         var _loc4_:int = 0;
         super.draw();
         if(isInvalid(InvalidationType.LAYOUT))
         {
            _loc2_ = this._allItems[0];
            _loc3_ = this._allItems.length;
            _loc4_ = 1;
            while(_loc4_ < _loc3_)
            {
               _loc1_ = this._allItems[_loc4_];
               _loc1_.y = Math.round(_loc2_.y + _loc2_.height + this._itemsOffsetsList[_loc4_ - 1]);
               _loc2_ = _loc1_;
               _loc4_++;
            }
            setSize(actualWidth,_loc1_.y + _loc1_.height);
            dispatchEvent(new Event(Event.RESIZE));
         }
      }
      
      private function renderHandler(param1:Event) : void
      {
         var _loc3_:CheckBox = null;
         var _loc2_:DisplayObject = param1.currentTarget as DisplayObject;
         if(_loc2_)
         {
            _loc2_.removeEventListener(Event.RENDER,this.renderHandler);
         }
         if(param1.currentTarget is CheckBox)
         {
            _loc3_ = CheckBox(param1.currentTarget);
            _loc3_.height = _loc3_.textField.height;
         }
         invalidateLayout();
      }
   }
}
