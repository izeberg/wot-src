package net.wg.gui.lobby.battleResults.commendation
{
   import flash.events.MouseEvent;
   import net.wg.gui.components.controls.Image;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.infrastructure.interfaces.entity.IUpdatable;
   
   public class CommendationButton extends SoundButtonEx implements IUpdatable
   {
      
      private static const _STATE_LOCKED_SELECTION:String = "lockedSelection";
      
      private static const _STATE_HIGHLIGHT:String = "highlight";
      
      private static const _STATE_UP:String = "up";
      
      private static const MUTED_SOUND_TYPES:Array = [MouseEvent.MOUSE_DOWN];
       
      
      public var image:Image;
      
      public var imageSelected:Image;
      
      public var imageGlow:Image;
      
      public function CommendationButton()
      {
         constraintsDisabled = true;
         preventAutosizing = true;
         mutedSoundTypes = MUTED_SOUND_TYPES;
         super();
         _stateMap[_STATE_LOCKED_SELECTION] = [_STATE_LOCKED_SELECTION];
         _stateMap[_STATE_HIGHLIGHT] = [_STATE_HIGHLIGHT];
      }
      
      public function update(param1:Object) : void
      {
         this.data = param1;
      }
      
      public function highlight(param1:Boolean) : void
      {
         if(param1)
         {
            this.setState(_STATE_HIGHLIGHT);
         }
         else if(enabled && _state != _STATE_LOCKED_SELECTION && _state == _STATE_HIGHLIGHT)
         {
            this.setState(_STATE_UP);
         }
      }
      
      override public function set data(param1:Object) : void
      {
         super.data = param1;
         var _loc2_:CommendationBtnData = CommendationBtnData(param1);
         this.image.source = _loc2_.iconPath;
         this.imageGlow.source = _loc2_.iconGlowPath;
         this.imageSelected.source = _loc2_.selectedIconPath;
      }
      
      override protected function onDispose() : void
      {
         this.image.dispose();
         this.image = null;
         this.imageSelected.dispose();
         this.imageSelected = null;
         this.imageGlow.dispose();
         this.imageGlow = null;
         super.onDispose();
      }
      
      public function selectAndDisable() : void
      {
         enabled = false;
         this.setState(_STATE_LOCKED_SELECTION);
      }
      
      override protected function setState(param1:String) : void
      {
         if(_state == _STATE_LOCKED_SELECTION)
         {
            return;
         }
         super.setState(param1);
      }
   }
}
