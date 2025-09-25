package net.wg.gui.notification.custom.pm3
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import net.wg.infrastructure.interfaces.IDisposableSprite;
   
   public class PM3DescriptionCompleted extends Sprite implements IDisposableSprite
   {
      
      private static const BOTTOM_PADDING:int = 10;
       
      
      public var statusTF:TextField = null;
      
      private var _isDisposed:Boolean = false;
      
      public function PM3DescriptionCompleted()
      {
         super();
         this.statusTF.text = App.utils.locale.makeString(SYSTEM_MESSAGES.PERSONALMISSION_AWARDSNOTIFICATION_MISSIONCOMPLETED);
      }
      
      public final function dispose() : void
      {
         this.statusTF = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      override public function get height() : Number
      {
         return super.height + BOTTOM_PADDING;
      }
   }
}
