package net.wg.gui.battle.views.epicDeploymentMap
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.infrastructure.base.SimpleDisposable;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class EpicDeploymentWarning extends SimpleDisposable
   {
       
      
      public var textTF:TextField = null;
      
      public var background:MovieClip = null;
      
      private var _text:String = "";
      
      private var _topPadding:int;
      
      public function EpicDeploymentWarning()
      {
         super();
         mouseEnabled = mouseChildren = false;
         this.textTF.autoSize = TextFieldAutoSize.LEFT;
         this._topPadding = this.textTF.y;
      }
      
      override protected function onDispose() : void
      {
         this.textTF = null;
         this.background = null;
         super.onDispose();
      }
      
      public function update(param1:String) : void
      {
         this._text = param1;
         this.textTF.text = this._text;
         this.background.height = this.textTF.height + this._topPadding * 2;
      }
      
      public function get hasText() : Boolean
      {
         return StringUtils.isNotEmpty(this._text);
      }
   }
}
