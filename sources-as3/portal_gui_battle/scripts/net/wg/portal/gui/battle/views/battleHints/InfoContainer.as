package net.wg.portal.gui.battle.views.battleHints
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.eventBattle.views.battleHints.data.HintInfoVO;
   import net.wg.gui.components.controls.Image;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class InfoContainer extends MovieClip implements IDisposable
   {
      
      private static const ICON_SCALE:Number = 0.5;
      
      private static const SHOW_FRAME_LABEL:String = "show";
      
      private static const OUT_SHOW_LABEL:String = "outShow";
       
      
      public var txtMessage:TextContainer = null;
      
      public var icon:Image = null;
      
      private var _disposed:Boolean = false;
      
      private var _data:HintInfoVO = null;
      
      public function InfoContainer()
      {
         super();
         this.icon.bitmap.scaleX = this.icon.bitmap.scaleY = ICON_SCALE;
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this._data = null;
         this.txtMessage.dispose();
         this.txtMessage = null;
         this.icon.dispose();
         this.icon = null;
      }
      
      public function hideHint() : void
      {
         gotoAndPlay(OUT_SHOW_LABEL);
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function showHint(param1:HintInfoVO) : void
      {
         if(param1 == null || this._data == param1)
         {
            return;
         }
         this._data = param1;
         if(StringUtils.isNotEmpty(param1.iconSource))
         {
            this.icon.source = param1.iconSource;
         }
         this.txtMessage.setText(param1.message);
         this.updateLayout();
         gotoAndPlay(SHOW_FRAME_LABEL);
      }
      
      private function updateLayout() : void
      {
         var _loc1_:Boolean = this._data != null && StringUtils.isNotEmpty(this._data.iconSource);
         this.icon.visible = _loc1_;
         this.txtMessage.useWithIconAlignment = _loc1_;
      }
   }
}
