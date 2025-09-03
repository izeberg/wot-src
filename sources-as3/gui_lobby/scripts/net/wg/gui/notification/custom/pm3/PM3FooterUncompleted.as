package net.wg.gui.notification.custom.pm3
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import net.wg.infrastructure.interfaces.IDisposableSprite;
   import net.wg.utils.ILocale;
   
   public class PM3FooterUncompleted extends Sprite implements IDisposableSprite
   {
      
      private static const BOTTOM_MARGIN:int = 10;
      
      private static const TEXT_HEIGHT_BOTTOM_PADDING:int = 4;
       
      
      public var statusTf:TextField = null;
      
      private var _isDisposed:Boolean = false;
      
      private var _locale:ILocale;
      
      public function PM3FooterUncompleted()
      {
         this._locale = App.utils.locale;
         super();
         this.statusTf.text = this._locale.makeString(SYSTEM_MESSAGES.PERSONALMISSION_AWARDSNOTIFICATION_NOTCOMPLETEDFOOTER);
         this.statusTf.height = this.statusTf.textHeight + TEXT_HEIGHT_BOTTOM_PADDING;
      }
      
      public final function dispose() : void
      {
         this._locale = null;
         this.statusTf = null;
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      override public function get height() : Number
      {
         return this.statusTf.y + this.statusTf.height + BOTTOM_MARGIN >> 0;
      }
   }
}
