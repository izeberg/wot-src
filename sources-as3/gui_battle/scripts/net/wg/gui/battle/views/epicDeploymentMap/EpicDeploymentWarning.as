package net.wg.gui.battle.views.epicDeploymentMap
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.EPIC_CONSTS;
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
      
      public function updateLane(param1:String, param2:String) : void
      {
         this._text = Values.EMPTY_STR;
         if(StringUtils.isNotEmpty(param2) && param1 != param2)
         {
            this._text = EPIC_BATTLE.DEPLOYMENTMAP_WARNING_1;
            if(param2 == EPIC_CONSTS.LANE_TOP)
            {
               this._text = EPIC_BATTLE.DEPLOYMENTMAP_WARNING_2;
            }
            else if(param1 == EPIC_CONSTS.LANE_TOP)
            {
               this._text = EPIC_BATTLE.DEPLOYMENTMAP_WARNING_3;
            }
         }
         this.textTF.text = this._text;
         this.background.height = this.textTF.height + this._topPadding * 2;
      }
      
      public function get hasText() : Boolean
      {
         return StringUtils.isNotEmpty(this._text);
      }
   }
}
