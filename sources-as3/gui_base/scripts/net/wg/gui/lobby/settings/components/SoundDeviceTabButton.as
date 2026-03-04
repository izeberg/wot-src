package net.wg.gui.lobby.settings.components
{
   import net.wg.data.constants.ComponentState;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.advanced.InviteIndicator;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.components.controls.UILoaderAlt;
   
   public class SoundDeviceTabButton extends SoundButtonEx
   {
      
      private static const ENABLE_ALPHA:Number = 1;
      
      private static const DISABLE_TEXT_ALPHA:Number = 0.3;
      
      private static const DISABLE_ICON_ALPHA:Number = 0.5;
      
      private static const DISABLE_MC_ALPHA:Number = 0.7;
       
      
      public var icon:UILoaderAlt = null;
      
      public var updateWaiting:InviteIndicator = null;
      
      private var _id:String = null;
      
      private var _speakerId:String = null;
      
      private var _prevState:String;
      
      public function SoundDeviceTabButton()
      {
         super();
         preventAutosizing = true;
         constraintsDisabled = true;
         disableMc.alpha = DISABLE_MC_ALPHA;
         this.hitArea = this.bgMc;
      }
      
      override protected function onDispose() : void
      {
         this.icon.dispose();
         this.icon = null;
         this.updateWaiting.dispose();
         this.updateWaiting = null;
         super.onDispose();
      }
      
      override protected function updateDisable() : void
      {
         super.updateDisable();
         this.icon.alpha = !!enabled ? Number(ENABLE_ALPHA) : Number(DISABLE_ICON_ALPHA);
         textField.alpha = !!enabled ? Number(ENABLE_ALPHA) : Number(DISABLE_TEXT_ALPHA);
      }
      
      override protected function updateText() : void
      {
         var _loc1_:Boolean = _label == null || _label == Values.EMPTY_STR;
         this.updateWaiting.visible = _loc1_;
         super.updateText();
      }
      
      override protected function setState(param1:String) : void
      {
         if((this._prevState == ComponentState.DOWN || this._prevState == ComponentState.RELEASE || this._prevState == ComponentState.OVER) && param1 == ComponentState.TOGGLE)
         {
            this._prevState = ComponentState.RELEASE;
            super.setState(ComponentState.RELEASE);
         }
         else
         {
            this._prevState = param1;
            super.setState(param1);
         }
      }
      
      public function iconSource(param1:String) : void
      {
         this.icon.source = param1;
      }
      
      public function get id() : String
      {
         return this._id;
      }
      
      public function set id(param1:String) : void
      {
         this._id = param1;
      }
      
      public function get speakerId() : String
      {
         return this._speakerId;
      }
      
      public function set speakerId(param1:String) : void
      {
         this._speakerId = param1;
      }
   }
}
