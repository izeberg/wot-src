package net.wg.gui.battle.views.epicDeploymentMap.components
{
   import flash.display.MovieClip;
   import flash.geom.Point;
   import flash.text.TextField;
   import flash.utils.Dictionary;
   import net.wg.data.constants.generated.EPIC_CONSTS;
   import net.wg.infrastructure.base.SimpleDisposable;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class EpicCurrentLaneContainer extends SimpleDisposable
   {
      
      private static const POSITIONS_BY_LANE:Dictionary = new Dictionary();
      
      private static const VERTICAL_LABEL:String = "vertical";
      
      private static const HORIZONTAL_LABEL:String = "horizontal";
      
      private static const TEXTS_BY_LANE:String = "#epic_battle:deploymentMap/lane/";
      
      {
         POSITIONS_BY_LANE[EPIC_CONSTS.LANE_LEFT] = new Point(0,285);
         POSITIONS_BY_LANE[EPIC_CONSTS.LANE_CENTER] = new Point(210,285);
         POSITIONS_BY_LANE[EPIC_CONSTS.LANE_RIGHT] = new Point(419,285);
         POSITIONS_BY_LANE[EPIC_CONSTS.LANE_TOP] = new Point(0,104);
      }
      
      public var activeLane:MovieClip = null;
      
      public var selectedLane:MovieClip = null;
      
      public var textTF:TextField = null;
      
      private var _currentLane:String = "";
      
      private var _selectedLane:String = "";
      
      public function EpicCurrentLaneContainer()
      {
         super();
         this.activeLane.visible = this.selectedLane.visible = this.textTF.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.activeLane = null;
         this.selectedLane = null;
         this.textTF = null;
         super.onDispose();
      }
      
      public function updateLane(param1:String, param2:String) : void
      {
         if(this._currentLane != param1 || this._selectedLane != param2)
         {
            this._currentLane = param1;
            this._selectedLane = param2;
            this.updateLayout();
         }
      }
      
      private function updateLayout() : void
      {
         var _loc1_:Point = null;
         var _loc2_:String = null;
         var _loc3_:MovieClip = null;
         this.textTF.visible = this.activeLane.visible = StringUtils.isNotEmpty(this._currentLane);
         if(this.activeLane.visible)
         {
            _loc1_ = POSITIONS_BY_LANE[this._currentLane];
            this.activeLane.x = _loc1_.x;
            this.activeLane.y = _loc1_.y;
            this.activeLane.gotoAndStop(this._currentLane == EPIC_CONSTS.LANE_TOP ? HORIZONTAL_LABEL : VERTICAL_LABEL);
            this.textTF.text = TEXTS_BY_LANE + this._currentLane.toLowerCase();
            if(this._currentLane == EPIC_CONSTS.LANE_TOP)
            {
               this.textTF.x = this.activeLane.x + (this.activeLane.width - this.textTF.width) >> 1;
            }
            else
            {
               this.textTF.x = this.activeLane.x - (Math.abs(this.activeLane.width - this.textTF.width) >> 1);
            }
         }
         this.selectedLane.visible = StringUtils.isNotEmpty(this._selectedLane) && this._currentLane != this._selectedLane;
         if(this.selectedLane.visible)
         {
            _loc1_ = POSITIONS_BY_LANE[this._selectedLane];
            this.selectedLane.x = _loc1_.x;
            this.selectedLane.y = _loc1_.y;
            _loc2_ = this._selectedLane == EPIC_CONSTS.LANE_TOP ? HORIZONTAL_LABEL : VERTICAL_LABEL;
            this.selectedLane.gotoAndStop(_loc2_);
            _loc3_ = this.selectedLane.getChildByName(_loc2_) as MovieClip;
            if(_loc3_)
            {
               _loc3_.gotoAndPlay(1);
            }
         }
      }
   }
}
