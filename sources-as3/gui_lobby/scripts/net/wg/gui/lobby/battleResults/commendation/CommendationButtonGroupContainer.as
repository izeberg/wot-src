package net.wg.gui.lobby.battleResults.commendation
{
   import flash.display.DisplayObject;
   import net.wg.data.constants.generated.PLAYER_SATISFACTION_RATING;
   import net.wg.gui.components.containers.GroupEx;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class CommendationButtonGroupContainer extends GroupEx
   {
       
      
      private var _highLightedIDs:Array;
      
      private var _selectedID:int = 0;
      
      public function CommendationButtonGroupContainer()
      {
         this._highLightedIDs = [];
         super();
      }
      
      public function get highlightButtons() : Array
      {
         return this._highLightedIDs;
      }
      
      public function set highlightButtons(param1:Array) : void
      {
         this._highLightedIDs = param1;
         invalidateData();
      }
      
      public function set selectedID(param1:int) : void
      {
         if(this._selectedID != param1)
         {
            this._selectedID = param1;
            invalidateData();
         }
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this.updateHighlights();
            this.applyChoice(this._selectedID);
         }
      }
      
      override public function removeChild(param1:DisplayObject) : DisplayObject
      {
         var _loc2_:DisplayObject = super.removeChild(param1);
         var _loc3_:CommendationButton = _loc2_ as CommendationButton;
         if(_loc3_)
         {
            _loc3_.removeEventListener(ButtonEvent.CLICK,this.onClick);
         }
         return _loc2_;
      }
      
      override public function addChild(param1:DisplayObject) : DisplayObject
      {
         var _loc2_:DisplayObject = super.addChild(param1);
         var _loc3_:CommendationButton = _loc2_ as CommendationButton;
         if(_loc3_)
         {
            _loc3_.addEventListener(ButtonEvent.CLICK,this.onClick,false,0,true);
         }
         return _loc2_;
      }
      
      private function onClick(param1:ButtonEvent) : void
      {
         var _loc2_:CommendationButton = CommendationButton(param1.target);
         var _loc3_:int = CommendationBtnData(_loc2_.data).btnID;
         this.selectedID = _loc3_;
         dispatchEvent(new CBGEvent(_loc3_));
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:Vector.<DisplayObject> = renderers;
         var _loc2_:int = 0;
         while(_loc2_ < _loc1_.length)
         {
            _loc1_[_loc2_].removeEventListener(ButtonEvent.CLICK,this.onClick);
            _loc2_++;
         }
         super.onDispose();
      }
      
      private function applyChoice(param1:int) : void
      {
         var _loc4_:CommendationButton = null;
         if(param1 == PLAYER_SATISFACTION_RATING.NONE)
         {
            return;
         }
         var _loc2_:Vector.<DisplayObject> = renderers;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_.length)
         {
            _loc4_ = CommendationButton(_loc2_[_loc3_]);
            if(param1 == CommendationBtnData(_loc4_.data).btnID)
            {
               _loc4_.selectAndDisable();
            }
            else
            {
               _loc4_.enabled = false;
            }
            _loc3_++;
         }
      }
      
      private function updateHighlights() : CommendationButton
      {
         var _loc4_:CommendationButton = null;
         var _loc1_:Vector.<DisplayObject> = renderers;
         var _loc2_:Boolean = this._selectedID != PLAYER_SATISFACTION_RATING.NONE;
         var _loc3_:int = 0;
         while(_loc3_ < _loc1_.length)
         {
            _loc4_ = CommendationButton(_loc1_[_loc3_]);
            if(_loc2_)
            {
               _loc4_.highlight(false);
            }
            else
            {
               _loc4_.highlight(this._highLightedIDs.indexOf(CommendationBtnData(_loc4_.data).btnID) != -1);
            }
            _loc3_++;
         }
         return _loc4_;
      }
   }
}
