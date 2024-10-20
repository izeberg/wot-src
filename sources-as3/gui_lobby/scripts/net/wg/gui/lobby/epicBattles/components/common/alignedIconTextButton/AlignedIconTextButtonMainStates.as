package net.wg.gui.lobby.epicBattles.components.common.alignedIconTextButton
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class AlignedIconTextButtonMainStates extends MovieClip implements IDisposable
   {
       
      
      public var textMc:MovieClip = null;
      
      private var _disposed:Boolean = false;
      
      public function AlignedIconTextButtonMainStates()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.textMc = null;
      }
      
      public function updateStatesWidth() : void
      {
         if(StringUtils.isNotEmpty(this.textMc.textField.text))
         {
            App.utils.commons.updateTextFieldSize(this.textMc.textField,true,false);
         }
         else
         {
            this.textMc.textField.width = 0;
         }
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
   }
}
